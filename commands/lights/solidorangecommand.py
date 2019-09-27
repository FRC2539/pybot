from wpilib.command.command import Command

import subsystems

class SolidOrangeCommand(Command):

    def __init__(self):
        super().__init__('Solid Orange')

        self.requires(subsystems.lights)

    def initialize(self):
        subsystems.lights.solidOrange()

    def execute(self):
        subsystems.lights.solidOrange()

    def end(self):
        subsystems.lights.off()
