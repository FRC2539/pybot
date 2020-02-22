from wpilib.command import Command

import robot


class LowerClimberCommand(Command):

    def __init__(self):
        super().__init__('Lower Climber')

        self.requires(robot.climber)

    def initialize(self):
        robot.climber.lowerClimber()

    def end(self):
        robot.climber.stop()
