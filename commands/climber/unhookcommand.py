from wpilib.command import Command

import robot

class UnhookCommand(Command):
    '''
    Start spinning the winch.
    '''

    def __init__(self):
        super().__init__('Unhook')

        self.requires(robot.climber)


    def initialize(self):
        robot.climber.hookUp()


    def end(self):
        robot.climber.stopHook()
