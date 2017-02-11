from commands.drive.movecommand import MoveCommand

import subsystems

class GoToLiftCommand(MoveCommand):

    def __init__(self):
        super().__init__(0, 'GoToLiftCommand')


    def initialize(self):
        self.distance = subsystems.gear.distanceToTarget() - 12
        super().initialize()
