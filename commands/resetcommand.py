from wpilib.command import InstantCommand

import robot

class ResetCommand(InstantCommand):
    '''
    Disable any running commands for all robot, except Monitor. This should
    be used to stop any motion and return the commands to a safe state. In
    general just requiring a subsystem will stop its current command. Additional
    resetting can be handled in the initialize method.
    '''

    def __init__(self):
        '''Require all active robot here.'''
        super().__init__('Reset')

        self.requires(robot.drivetrain)
