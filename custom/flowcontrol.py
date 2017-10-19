from wpilib.command.commandgroup import CommandGroup
from commands.conditionalcommand import ConditionalCommand
from wpilib.command.instantcommand import InstantCommand
from commandbased.cancelcommand import CancelCommand

import inspect

'''
These functions can be used to make programming CommandGroups much more
intuitive. For more information, check each method's docstring.
'''

def _getCommandGroup():
    '''
    Does some rather ugly stack inspection to find out which CommandGroup the
    calling function was triggered from.
    '''
    # https://stackoverflow.com/a/14694234
    stack = inspect.stack()
    frame = stack[2].frame
    while 'self' not in frame.f_locals:
        frame = frame.f_back
        if frame is None:
            raise ValueError(
                'Could not find calling class for %s' %
                stack[1].function.__name__
            )

    cg = frame.f_locals['self']
    if not isinstance(cg, CommandGroup):
        raise ValueError(
            '%s may not be use outside of a CommandGroup' %
            stack[1].function.__name__
        )

    return cg


def _getSource(parent):
    'Finds the highest level CommandGroup of parent'

    try:
        return parent._source
    except AttributeError:
        return parent


def _buildCommandGroup(func, parent):
    'Turns the given function into a full CommandGroup.'

    source = _getSource(parent)

    cg = CommandGroup(func.__name__)
    cg._source = source
    func(cg)

    for reqt in cg.getRequirements():
        source.requires(reqt)

    return cg


def _restartWhile(self):
    '''
    Replaces isFinished for a ConditionalCommand in a WHILE loop, to keep it
    running.
    '''
    finished = super().isFinished()

    if finished:
        if self.condition:
            self.onTrue.start()
            return False

    return finished


def _popIfStack(cg):
    '''
    We buffer conditionals until the last moment so we don't have trouble with
    Commands being locked when they're added to a CommandGroup.
    '''
    if cg._ifStack:
        top = cg._ifStack.pop(0)
        cmd = None
        for x in reversed(cg._ifStack):
            if x[0]:
                cmd = ConditionalCommand('flowcontrolELIF', x[1], cmd)
                cmd.condition = x[0]

            else:
                cmd = x[1]

        cmd = ConditionalCommand('flowcontrolIF', top[1], cmd)
        cmd.condition = top[0]

        cg._addSequential(cmd)
        cg._ifStack = None


# These _hook methods ensure we always add our buffered conditions
def _hookSequential(self, cmd, timeout=None):
    _popIfStack(self)
    self._addSequential(cmd, timeout)


def _hookParallel(self, cmd, timeout=None):
    _popIfStack(self)
    self._addParallel(cmd, timeout)


def _hookStart(self):
    _popIfStack(self)
    self._start()


def _hookParent(self, parent):
    _popIfStack(self)
    self._setParent(parent)


def _hookCommandGroup(cg):
    '''Override some methods of the CommandGroup to add buffered commands'''

    try:
        cg._ifStack
        return
    except AttributeError:
        pass

    cg._addSequential = cg.addSequential
    cg._addParallel = cg.addParallel
    cg._start = cg.start
    cg._setParent = cg.setParent

    cg.addSequential = _hookSequential.__get__(cg)
    cg.addParallel = _hookParallel.__get__(cg)
    cg.start = _hookStart.__get__(cg)
    cg.setParent = _hookParent.__get__(cg)


def IF(condition):
    '''
    Use as a decorator for a function. That function will be placed into a
    CommandGroup and run inside a ConditionalCommand with the given condition.
    The decorated function must accept one positional argument that will be used
    as its 'self'.
    '''

    def flowcontrolIF(func):
        parent = _getCommandGroup()
        _hookCommandGroup(parent)

        cg = _buildCommandGroup(func, parent)
        parent._ifStack = [(condition, cg)]

    return flowcontrolIF


def ELIF(condition):
    '''
    Use as a decorator for a function. That function will be placed into a
    CommandGroup which will be triggered by a ConditionalCommand that uses the
    passed condition. That ConditionalCommand will then be added as the onFalse
    for the ConditionalCommand created by a previous IF or ELIF.
    '''

    def flowcontrolELIF(func):
        parent = _getCommandGroup()

        cg = _buildCommandGroup(func, parent)
        parent._ifStack.append((condition, cg))

    return flowcontrolELIF


def ELSE(func):
    '''
    Use as a decorator for a function. That function will be placed into a
    CommandGroup which will be added as the onFalse for the ConditionalCommand
    created by a previous IF or ELIF.
    '''

    parent = _getCommandGroup()
    cg = _buildCommandGroup(func, parent)
    parent._ifStack.append((None, cg))

    _popIfStack(parent)


def WHILE(condition):
    '''
    Use as a decorator for a function. That function will be placed into a
    CommandGroup, which will be added to a ConditionalCommand. It will be
    modified to restart itself automatically.
    '''

    def flowcontrolWHILE(func):
        parent = _getCommandGroup()
        source = _getSource(parent)

        try:
            parentLoop = source._currentLoop
        except AttributeError:
            parentLoop = None

        cg = CommandGroup(func.__name__)

        cg._source = source
        source._currentLoop = cg
        func(cg)

        for reqt in cg.getRequirements():
            source.requires(reqt)

        cond = ConditionalCommand('flowcontrolWHILE', cg)
        cond.condition = condition
        cond.isFinished = _restartWhile.__get__(cond)
        cond._parentLoop = parentLoop

        parent.addSequential(cond)

        cg.conditionalCommand = cond
        source._currentLoop = parentLoop

    return flowcontrolWHILE


def RETURN():
    '''
    Calling this function will end the source CommandGroup immediately.
    '''

    parent = _getCommandGroup()
    source = _getSource(parent)

    parent.addSequential(CancelCommand(source))


def BREAK(steps=1):
    '''
    Calling this function will end the loop that contains it. Pass an integer to
    break out of that number of nested loops.
    '''

    if steps < 1:
        raise ValueError('Steps to BREAK cannot be < 1')

    parent = _getCommandGroup()
    source = _getSource(parent)

    try:
        loop = source._currentLoop
    except AttributeError:
        raise ValueError('Cannot BREAK outside of a loop')

    if loop is None:
        raise ValueError('Cannot BREAK outside of a loop')

    step = 1
    while steps > step:
        loop = loop.conditionalCommand._parentLoop

        if loop is None:
            raise ValueError(
                'BREAK %i not possible with loop depth %i' %
                (steps, step)
            )

        step += 1

    breakCmd = InstantCommand('BREAK')
    breakCmd.initialize = lambda: loop.conditionalCommand._cancel()

    parent.addSequential(breakCmd)
