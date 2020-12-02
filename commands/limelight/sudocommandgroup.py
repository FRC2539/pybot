from wpilib.command import CommandGroup
import commandbased.flowcontrol as fc

from commands.hood.hoodlimelightcommand import HoodLimelightCommand
from commands.hood.stevenhoodlimelightcommand import StevenHoodLimelightCommand
from commands.shooter.stevenshooterlimelightcommand import StevenShooterLimelightCommand
from commands.turret.turretlimelightcommand import TurretLimelightCommand
from commands.turret.camtranturretlimelight import CamTranTurretLimelight
from commands.shooter.shootwhenreadycommand import ShootWhenReadyCommand
from commands.revolver.firesequencecommand import FireSequenceCommand

class SudoCommandGroup(CommandGroup):

    def __init__(self, autoEnd=True):
        super().__init__('Sudo')

        # Add commands here with self.addSequential() and self.addParallel()
        #self.addParallel(CamTranTurretLimelight())
        self.addParallel(TurretLimelightCommand())
        self.addParallel(StevenHoodLimelightCommand())
        self.addParallel(StevenShooterLimelightCommand())
        self.addSequential(FireSequenceCommand(autoEnd))
        #self.addParallel(ShootWhenReadyCommand())

