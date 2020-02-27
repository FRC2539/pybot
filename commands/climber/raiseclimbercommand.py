from wpilib.command import Command

import robot


class RaiseClimberCommand(Command):

    def __init__(self):
        super().__init__('Raise Climber')

        self.requires(robot.climber)

    def initialize(self):
        robot.climber.raiseClimber()

    def execute(self):
        robot.climber.raiseClimber()

    def end(self):
        robot.climber.stop()
