from .logitechdualshock import LogitechDualShock
from . import logicalaxes

from custom.config import Config

from commands.drivetrain.drivecommand import DriveCommand
from commands.drivetrain.playmusiccommand import PlayMusicCommand
from commands.resetcommand import ResetCommand

from commands.intake.intakecommand import IntakeCommand
from commands.intake.outtakecommand import OutakeCommand
from commands.intake.clearjamtwocommand import ClearJamTwoCommand
from commands.intake.stopeverythingcommand import StopEverythingCommand

from commands.colorwheel.getcolorcommand import GetColorCommand

from commands.ballsystem.runallcommand import RunAllCommand
from commands.ballsystem.runindexwithverticalcommand import RunIndexWithVerticalCommand
from commands.ballsystem.runlowercommand import RunLowerCommand
from commands.ballsystem.clearjamcommand import ClearJamCommand

from commands.ballsystem.slowrunballflowcommandgroup import SlowRunBallFlowCommandGroup
from commands.ballsystem.loadballfromhoppercommand import LoadBallFromHopperCommand
from commands.ballsystem.rununtilloadedcommand import RunUntilLoadedCommand

from commands.ballsystem.reversehorizontalcommand import ReverseHorizontalCommand

from commands.ballsystem.runballflowcommandgroup import RunBallFlowCommandGroup

from commands.pneumaticsystems.runcompressor import RunCompressorCommand

from commands.hood.raisehoodcommand import RaiseHoodCommand
from commands.hood.lowerhoodcommand import LowerHoodCommand
from commands.hood.sethoodcommand import SetHoodCommand
from commands.hood.hoodtestcommand import hoodTestCommand
from commands.hood.updatehoodnetworktablescommand import UpdateHoodNetworkTablesCommand
from commands.hood.hoodlimelightcommand import HoodLimelightCommand
from commands.hood.setlaunchanglecommand import SetLaunchAngleCommand

from commands.limelight.lltestcommand import llTestCommand
from commands.limelight.finitereecommand import finiteReeCommand

from commands.shooter.shootcommand import ShootCommand
from commands.shooter.controlledshootcommand import ControlledShootCommand
from commands.shooter.reverseshootercommand import ReverseShooterCommand
from commands.shooter.farshotcommandgroup import FarShotCommandGroup

from commands.turret.turretlimelightcommand import TurretLimelightCommand

from commands.pneumaticsystems.extendclimberpistoncommand import ExtendClimberPistonCommand
from commands.limelight.sudocommandgroup import SudoCommandGroup

def init():
    '''
    Declare all controllers, assign axes to logical axes, and trigger
    commands on various button events. Available event types are:
        - whenPressed
        - whileHeld: cancelled when the button is released
        - whenReleased
        - toggleWhenPressed: start on first press, cancel on next
        - cancelWhenPressed: good for commands started with a different button
    '''

    # The controller for driving the robot
    driveController = LogitechDualShock(0)

    logicalaxes.driveX = driveController.LeftX
    logicalaxes.driveY = driveController.LeftY
    logicalaxes.driveRotate = driveController.RightX

    driveController.Back.whenPressed(ResetCommand())

    driveController.A.toggleWhenPressed(RunUntilLoadedCommand())
    driveController.X.toggleWhenPressed(LoadBallFromHopperCommand())
    driveController.B.whenPressed(OutakeCommand())


    #driveController.Y.toggleWhenPressed(TurretLimelightCommand())

    driveController.RightBumper.whileHeld(RaiseHoodCommand())
    driveController.RightTrigger.whileHeld(LowerHoodCommand())

    driveController.Start.toggleWhenPressed(RunCompressorCommand())

    driveController.LeftBumper.toggleWhenPressed(SetHoodCommand(10))

    # The controller for non-driving subsystems of the robot
    operatorController = LogitechDualShock(1)

    logicalaxes.turretX = operatorController.RightX

    operatorController.A.toggleWhenPressed(RunBallFlowCommandGroup())
    operatorController.LeftJoystick.toggleWhenPressed(SlowRunBallFlowCommandGroup())

    operatorController.X.toggleWhenPressed(ClearJamTwoCommand())
    operatorController.Y.toggleWhenPressed(ReverseShooterCommand())
    operatorController.B.toggleWhenPressed(ClearJamCommand())

    operatorController.RightBumper.whileHeld(RaiseHoodCommand())
    operatorController.RightTrigger.whileHeld(LowerHoodCommand())

    operatorController.Start.toggleWhenPressed(FarShotCommandGroup())

    operatorController.LeftTrigger.toggleWhenPressed(ShootCommand(4200))
    operatorController.LeftBumper.toggleWhenPressed(SudoCommandGroup())

    operatorController.Back.whenPressed(StopEverythingCommand())
