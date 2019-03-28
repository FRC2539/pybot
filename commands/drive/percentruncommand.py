from wpilib.command import Command

import subsystems

class PercentRunCommand(Command):

    def __init__(self, percent):
        super().__init__('PercentRunCommand %s')

        self.requires(subsystems.drivetrain)
        self.percent = percent / 100

    def initialize(self):
        subsystems.drivetrain.percentOutputMove(self.percent)

    def end(self):
        subsystems.drivetrain.stop()
