from wpilib.command import Command

import robot

class SafeElevateClimberCommand(Command):

    def __init__(self):
        super().__init__('Safe Elevate Climber')

        self.requires(robot.climber)

    def initialize(self):
        if robot.climber.isClimbLegal():
            robot.climber.elevateClimber()

    def execute(self):
        if robot.climber.isClimbLegal():
            robot.climber.elevateClimber()
        else:
            robot.climber.stop()

    def end(self):
        robot.climber.stop()