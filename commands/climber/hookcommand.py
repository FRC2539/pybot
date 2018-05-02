from wpilib.command import Command

import robot

class HookCommand(Command):
    '''
    Start spinning the winch.
    '''

    def __init__(self):
        super().__init__('Hook')

        self.requires(robot.climber)

    def initialize(self):
        robot.climber.hookDown()


    def end(self):
        robot.climber.stopHook()
