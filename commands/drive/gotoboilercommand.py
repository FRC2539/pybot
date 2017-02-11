from .movecommand import MoveCommand

import subsystems

class GoToBoilerCommand(MoveCommand):

    def __init__(self):
        super().__init__(0, 'GoToBoilerCommand')


    def initialize(self):
        self.distance = subsystems.shooter.distanceToTarget() - 12
        super().initialize()
