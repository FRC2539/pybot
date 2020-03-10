import commandbased.flowcontrol as fc

from commands.limelight.ogsudocommandgroup import OgSudoCommandGroup
from commands.turret.setturretcommand import SetTurretCommand
from commands.limelight.sudocommandgroup import SudoCommandGroup

class TurretStartCommandGroup(fc.CommandFlow):

    def __init__(self):
        super().__init__('Turret Start')

        # Add commands here with self.addSequential() and self.addParallel()
        self.addSequential(SetTurretCommand(2100), 1) # starts 100 ticks less becsause we are a little far left.
        self.addSequential(OgSudoCommandGroup())
