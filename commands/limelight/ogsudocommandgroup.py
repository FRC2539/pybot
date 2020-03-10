import commandbased.flowcontrol as fc

from commands.hood.hoodlimelightcommand import HoodLimelightCommand
from commands.turret.turretlimelightcommand import TurretLimelightCommand

class OgSudoCommandGroup(fc.CommandFlow):

    def __init__(self):
        super().__init__('Og Sudo')

        # Add commands here with self.addSequential() and self.addParallel()

        self.addParallel(HoodLimelightCommand())
        self.addParallel(TurretLimelightCommand())
