from wpilib.command import Command

import robot

class ClimbCommand(Command):
    '''
    Start spinning the winch.
    '''

    def __init__(self):
        super().__init__('Climb')

        self.requires(robot.climber)


    def initialize(self):
        robot.climber.startWinch()


    def end(self):
        robot.climber.stopWinch()
