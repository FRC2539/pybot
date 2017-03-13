from wpilib.command import Command

import subsystems

class ClearFuelCommand(Command):

    def __init__(self):
        super().__init__('Clear Fuel')

        self.requires(subsystems.pickup)


    def initialize(self):
        subsystems.pickup.run(-0.5)


    def end(self):
        subsystems.pickup.stop()

