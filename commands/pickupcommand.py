from wpilib.command import Command

import subsystems

class PickupCommand(Command):
    # Initialize the named command.
    def __init__(self):
        super().__init__('PickupCommand)

        self.requires(subsystems.pickup)

    def initialize(self):
        subsystems.pickup.startBallPickup()

    def end(self):
        subsystems.pickup.stop()
