from wpilib.command import InstantCommand

import robot


class ResetEncodersCommand(InstantCommand):

    def __init__(self):
        super().__init__('Reset Encoders')

        self.requires(robot.drivetrain)

    def initialize(self):
        robot.drivetrain.resetEncoders()


