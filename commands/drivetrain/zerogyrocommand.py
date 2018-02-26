from wpilib.command.instantcommand import InstantCommand

import subsystems

class ZeroGyroCommand(InstantCommand):

    def __init__(self):
        super().__init__('Zero Gyro')

        self.requires(subsystems.drivetrain)


    def initialize(self):
        subsystems.drivetrain.resetGyro()
