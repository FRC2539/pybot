from wpilib.command.command import Command

import subsystems

class SolidGreenCommand(Command):

    def __init__(self):
        super().__init__('solidgreen')

        self.requires(subsystems.lights)

    def initialize(self):
        subsystems.lights.solidGreen()

    def execute(self):
        subsystems.lights.solidGreen()

    def end(self):
        subsystems.lights.off()
