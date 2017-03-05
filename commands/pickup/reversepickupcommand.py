from wpilib.command import Command

import subsystems

class ReversePickupCommand(Command):
    # Initialize the named command.
    def __init__(self):
        super().__init__('ReversePickupCommand')

        self.requires(subsystems.pickup)

    def initialize(self):
        subsystems.pickup.reverseBallPickup()

    def end(self):
        subsystems.pickup.stop()

