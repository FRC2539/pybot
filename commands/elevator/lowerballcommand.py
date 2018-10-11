from wpilib.command.command import Command

import robot

class LowerBallCommand(Command):

    def __init__(self):
        super().__init__('Lower Ball')

        self.requires(robot.elevator)

    def initialize(self):
        robot.elevator.fastLower()

    def end(self):
        robot.elevator.stop()
