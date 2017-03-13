from wpilib.command import Command

import subsystems

class PickupCommand(Command):

    def __init__(self):
        super().__init__('PickupCommand')

        self.requires(subsystems.pickup)


    def initialize(self):
        subsystems.pickup.run(0.7)


    def end(self):
        subsystems.pickup.stop()
