from commands.drive.turncommand import TurnCommand

import subsystems

class TurnToLiftCommand(TurnCommand):
    def __init__(self):
        super().__init__(0, 'TurnToLiftCommand')

    def initialize(self):
        self.distance = subsystems.gear.offsetFromCenter()
        super().initialize()
