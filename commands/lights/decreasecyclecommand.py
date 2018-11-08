from wpilib.command.instantcommand import InstantCommand

import subsystems

class DecreaseCycleCommand(InstantCommand):

    def __init__(self):
        super().__init__('Cycle Lights')

        self.requires(subsystems.lights)

    def initialize(self):
        subsystems.lights.decreasecycle()

    def end(self):
        subsystems.lights.off()
