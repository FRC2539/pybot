from wpilib.command.instantcommand import InstantCommand

import robot

class ResetEncoderCommand(InstantCommand):

    def __init__(self):
        super().__init__('Reset Encoder')

        self.requires(robot.drivetrain)

    def initialize(self):
        robot.drivetrain.resetEncoders()
