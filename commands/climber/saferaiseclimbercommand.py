from wpilib.command import Command

import robot

class SafeRaiseClimberCommand(Command):

    def __init__(self):
        super().__init__('Safe Raise Climber')

        self.requires(robot.climber)

    def initialize(self):
        if robot.climber.isClimbLegal():
            robot.climber.raiseClimber()

    def execute(self):
        if robot.climber.isClimbLegal():
            robot.climber.raiseClimber()
        else:
            robot.climber.stop()

    def end(self):
        robot.climber.stop()