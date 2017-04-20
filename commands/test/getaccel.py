import subsystems

from wpilib.command.instantcommand import InstantCommand

class GetAccel(InstantCommand):

    def __init__(self):
        super().__init__('GetAccel')
        self.requires(subsystems.drivetrain)

    def initialize(self):
        print(subsystems.drivetrain.getAcceleration())
