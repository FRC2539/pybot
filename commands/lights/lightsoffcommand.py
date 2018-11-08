from wpilib.command.command import Command

import subsystems

class LightsOffCommand(Command):

    def __init__(self):
        super().__init__('Lights Off')

        self.requires(subsystems.lights)

    def initialize(self):
        subsystems.lights.off()
