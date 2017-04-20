import subsystems

from wpilib.command.instantcommand import InstantCommand

class PrintUltrasonic(InstantCommand):

    def __init__(self):
        super().__init__('PrintUltrasonic')

    def initialize(self):
        print(subsystems.drivetrain.getFrontClearance())
