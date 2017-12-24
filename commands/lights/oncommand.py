from wpilib.command import Command

import subsystems

class OnCommand(Command):
    def __init__(self, lightID):
        super().__init__('Enable Light %d' % lightID)

        self.requires(subsystems.lights)
        self.ID = lightID


    def initialize(self):
        subsystems.lights.on(self.ID)


    def end(self):
        subsystems.lights.off(self.ID)
