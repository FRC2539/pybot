from commands.drive.movecommand import MoveCommand

import subsystems

# Move to the lift.
class GoToLiftCommand(MoveCommand):

    def __init__(self):
        super().__init__(0, 'GoToLiftCommand')


    def initialize(self):
        self.distance = subsystems.gear.distanceToTarget() - 3
        super().initialize()
