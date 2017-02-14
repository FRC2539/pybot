from commands.drive.turncommand import TurnCommand

import subsystems

class TurnToBoilerCommand(TurnCommand):
    def __init__(self):
        super().__init__(0, 'TurnToBoilerCommand')

    def initialize(self):
        self.distance = subsystems.shooter.offsetFromCenter()
        super().initialize()
