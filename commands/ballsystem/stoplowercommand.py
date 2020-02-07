from wpilib.command import Command

import robot

class StopLowerCommand(Command):

    def __init__(self):
        super().__init__('Stop Lower')

        self.requires(robot.ballsystem)

    def initialize(self):
        robot.ballsystem.stopLowerConveyor()
