from wpilib.command import Command

import subsystems

class PickupCommand(Command):

    def __init__(self):
        super().__init__('PickupCommand')

        self.requires(subsystems.pickup)


    def initialize(self):
        subsystems.pickup.run(0.9)


    def end(self):
        subsystems.pickup.stop()
