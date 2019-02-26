from wpilib.command.command import Command

import robot

class PreciseModeCommand(Command):

    def __init__(self):
        super().__init__('Precise Mode')

    def initialize(self):
        self.original = robot.drivetrain.speedLimit
        robot.drivetrain.setSpeedLimit(int(self.original) / 2)


    def end(self):
        robot.drivetrain.setSpeedLimit(self.original)
