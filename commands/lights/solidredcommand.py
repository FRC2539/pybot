from wpilib.command.command import Command

import subsystems

class SolidRedCommand(Command):

    def __init__(self):
        super().__init__('Solid Red')

        self.requires(subsystems.lights)

    def initialize(self):
        subsystems.lights.solidRed()

    def execute(self):
        subsystems.lights.solidRed()

    def end(self):
        subsystems.lights.off()
