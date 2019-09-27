from wpilib.command.instantcommand import InstantCommand

import subsystems

class IncreaseCycleCommand(InstantCommand):

    def __init__(self):
        super().__init__('Increase Cycle')

        self.requires(subsystems.lights)

    def initialize(self):
        subsystems.lights.increaseCycle()

    def end(self):
        subsystems.lights.off()
