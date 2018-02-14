from wpilib.command.instantcommand import InstantCommand

import subsystems

class ResetTiltCommand(InstantCommand):

    def __init__(self):
        super().__init__('Set Tilt to 0')

        self.requires(subsystems.drivetrain)
        self.setRunWhenDisabled(True)


    def initialize(self):
        subsystems.drivetrain.resetTilt()
