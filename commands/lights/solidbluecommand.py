from wpilib.command.command import Command

import subsystems

class SolidBlueCommand(Command):

    def __init__(self):
        super().__init__('solidblue')

        self.requires(subsystems.lights)

    def initialize(self):
        subsystems.lights.solidBlue()

    def execute(self):
        subsystems.lights.solidBlue()

    def end(self):
        subsystems.lights.off()
