from wpilib.command.commandgroup import CommandGroup
from wpilib.command.conditionalcommand import ConditionalCommand
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


def IF(condition):
    '''
    Use as a decorator for a function. That function will be placed into a
    CommandGroup and run inside a ConditionalCommand with the given condition.
    The decorated function must accept one positional argument that will be used
    as its 'self'.
    '''

    def flowcontrolIF(func):
        parent = _getCommandGroup()

        cg = _buildCommandGroup(func, parent)

        cond = ConditionalCommand('flowcontrolIF', cg)
        cond.condition = condition

        parent.addSequential(cond)

        parent._ifStack = [cond]

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

        # Determine which conditional command to branch from
        try:
            cond = parent._ifStack[-1]
        except AttributeError:
            raise ValueError('Cannot have an ELIF without an active IF')

        try:
            branchCmd = parent.commands[-1].command
        except KeyError:
            raise ValueError('Cannot perform ELIF before IF')

        if branchCmd is not parent._ifStack[0]:
            raise ValueError('There cannot be Commands between IF and ELIF')

        # Create new command group with decorated function
        cg = _buildCommandGroup(func, parent)

        # Add command group to a new conditional command
        elseCond = ConditionalCommand('flowcontrolELIF', cg)
        elseCond.condition = condition

        # Make the new conditional command the "false" branch of the conditional
        # command we found earlier.
        cond.onFalse = elseCond

        # Store new conditional command so we can branch off it more if needed
        parent._ifStack.append(elseCond)

    return flowcontrolELIF


def ELSE(func):
    '''
    Use as a decorator for a function. That function will be placed into a
    CommandGroup which will be added as the onFalse for the ConditionalCommand
    created by a previous IF or ELIF.
    '''

    parent = _getCommandGroup()

    try:
        cond = parent._ifStack[-1]
    except AttributeError:
        raise ValueError('Cannot have an ELSE without an active IF')

    try:
        branchCmd = parent.commands[-1].command
    except KeyError:
        raise ValueError('Cannot perform ELSE before IF')

    if branchCmd is not parent._ifStack[0]:
        raise ValueError('There cannot be Commands between IF and ELSE')

    cg = _buildCommandGroup(func, parent)

    cond.onFalse = cg

    # Prevent any other ELSE or ELIF from using this ConditionalCommand
    del parent._ifStack


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
        cond.isFinished = _restartWhile
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
