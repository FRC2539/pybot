import commandbased.flowcontrol as fc

from commands.turret.turretfieldorientedcommand import TurretFieldOrientedCommand
from commands.turret.movefieldanglecommand import MoveFieldAngleCommand

class FieldCommandGroup(fc.CommandFlow):

    def __init__(self):
        super().__init__('Field')

        # Add commands here with self.addSequential() and self.addParallel()

        self.addParallel(TurretFieldOrientedCommand())
        self.addParallel(MoveFieldAngleCommand())
