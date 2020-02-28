from wpilib.command import Command

import robot

class ElevateClimberCommand(Command):

    def __init__(self):
        super().__init__('Elevate Climber')

        self.requires(robot.climber)

    def initialize(self):
        robot.climber.elevateClimber()

    def execute(self):
        robot.climber.elevateClimber()

    def end(self):
        robot.climber.stop()
