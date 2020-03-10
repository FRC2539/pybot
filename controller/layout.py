from .logitechdualshock import LogitechDualShock
from . import logicalaxes

from custom.config import Config

from commands.drivetrain.gyromovecommand import GyroMoveCommand
from commands.drivetrain.drivecommand import DriveCommand
from commands.drivetrain.playmusiccommand import PlayMusicCommand
from commands.drivetrain.drivebaselimelightcommand import DriveBaseLimelightCommand
from commands.drivetrain.precisespeedcommand import PreciseSpeedCommand

from commands.resetcommand import ResetCommand

from commands.intake.intakecommand import IntakeCommand
from commands.intake.outtakecommand import OutakeCommand
from commands.intake.clearjamtwocommand import ClearJamTwoCommand
from commands.intake.stopeverythingcommand import StopEverythingCommand
from commands.intake.quickreversecommand import QuickReverseCommand

from commands.colorwheel.runupuntilimpactcommand import RunUpUntilImpactCommand
from commands.colorwheel.rundownuntilimpactcommand import RunDownUntilImpactCommand
from commands.colorwheel.getcolorcommand import GetColorCommand

from commands.colorwheel.autospinwheel import AutoSpinWheelCommand
from commands.colorwheel.drivewheelcommand import DriveWheelCommand
from commands.colorwheel.reversewheelcommand import ReverseWheelCommand

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

from commands.hood.tunedownhoodcommand import TuneDownHoodCommand
from commands.hood.tuneuphoodcommand import TuneUpHoodCommand
from commands.hood.raisehoodcommand import RaiseHoodCommand
from commands.hood.lowerhoodcommand import LowerHoodCommand
from commands.hood.sethoodcommand import SetHoodCommand
from commands.hood.hoodtestcommand import hoodTestCommand
from commands.hood.updatehoodnetworktablescommand import UpdateHoodNetworkTablesCommand
from commands.hood.hoodlimelightcommand import HoodLimelightCommand
from commands.hood.setlaunchanglecommand import SetLaunchAngleCommand
from commands.hood.experimentalcommand import ExperimentalCommand

from commands.limelight.lltestcommand import llTestCommand
from commands.limelight.finitereecommand import finiteReeCommand

from commands.shooter.shootcommand import ShootCommand
from commands.shooter.controlledshootcommand import ControlledShootCommand
from commands.shooter.reverseshootercommand import ReverseShooterCommand
from commands.shooter.farshotcommandgroup import FarShotCommandGroup
from commands.shooter.closeshotcommandgroup import CloseShotCommandGroup
from commands.shooter.superdanksmartshootcommand import SuperDankSmartShootCommand

from commands.turret.turretlimelightcommand import TurretLimelightCommand
from commands.turret.setturretcommand import SetTurretCommand
from commands.turret.turretfieldorientedcommand import TurretFieldOrientedCommand
from commands.turret.movefieldanglecommand import MoveFieldAngleCommand

from commands.pneumaticsystems.extendclimberpistoncommand import ExtendClimberPistonCommand
from commands.limelight.sudocommandgroup import SudoCommandGroup
from commands.limelight.aimturretdrivebasecommand import AimTurretDrivebaseCommand

from commands.winch.pullwinchcommand import PullWinchCommand
from commands.winch.releasewinchcommand import ReleaseWinchCommand

from commands.climber.raiseclimbercommand import RaiseClimberCommand
from commands.climber.lowerclimbercommand import LowerClimberCommand
from commands.climber.elevateclimbercommand import ElevateClimberCommand

from commands.diagnosticstestcommand import DiagnosticsTestCommand
from commands.drivetrain.zerogyrocommand import ZeroGyroCommand
from commands.drivetrain.setfieldpositioncommand import SetFieldPositionCommand

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
    driveController.B.toggleWhenPressed(OutakeCommand())
    driveController.Y.toggleWhenPressed(DriveCommand(4000)) # really jank

    driveController.LeftBumper.whileHeld(RaiseHoodCommand())
    driveController.LeftTrigger.whileHeld(LowerHoodCommand())

    driveController.LeftJoystick.whileHeld(PullWinchCommand())
    driveController.RightJoystick.whileHeld(RaiseClimberCommand())

    driveController.RightBumper.whileHeld(ElevateClimberCommand())
    driveController.RightTrigger.whileHeld(LowerClimberCommand())

    driveController.Start.toggleWhenPressed(RunUpUntilImpactCommand())
    driveController.Back.toggleWhenPressed(RunDownUntilImpactCommand())

#    driveController.DPadUp.whileHeld(DriveBaseLimelightCommand())
    driveController.DPadDown.toggleWhenPressed(AutoSpinWheelCommand())
    driveController.DPadUp.whenPressed(ZeroGyroCommand())
    driveController.DPadRight.whileHeld(DriveWheelCommand())
    driveController.DPadLeft.whileHeld(ReverseWheelCommand())
    #driveController.DPadUp.whileHeld(SetFieldPositionCommand(0, 120))

    # The controller for non-driving subsystems of the robot
    operatorController = LogitechDualShock(1)

    logicalaxes.turretX = operatorController.RightX

    operatorController.A.toggleWhenPressed(RunBallFlowCommandGroup())

    operatorController.LeftJoystick.toggleWhenPressed(ExperimentalCommand())
    operatorController.RightJoystick.whenPressed(RunUpUntilImpactCommand())

    operatorController.X.whenPressed(QuickReverseCommand())
    #operatorController.Y.whenPressed(ZeroGyroCommand())
    operatorController.Y.toggleWhenPressed(ReverseShooterCommand())
    operatorController.B.toggleWhenPressed(ClearJamCommand())

    operatorController.RightBumper.whileHeld(RaiseHoodCommand())
    operatorController.RightTrigger.whileHeld(LowerHoodCommand())

    #operatorController.DPadUp.whileHeld(FlipColorwheelUpCommand())

    #operatorController.LeftTrigger.toggleWhenPressed(ShootCommand(4200))
    operatorController.LeftTrigger.toggleWhenPressed(llTestCommand())
    operatorController.LeftBumper.toggleWhenPressed(SudoCommandGroup())

    operatorController.DPadUp.toggleWhenPressed(TurretFieldOrientedCommand())
    operatorController.DPadLeft.whileHeld(MoveFieldAngleCommand(-10))

    operatorController.DPadDown.toggleWhenPressed(ShootCommand(2400))
    operatorController.DPadRight.whileHeld(MoveFieldAngleCommand(10))#2400 and all the way down
    operatorController.Back.whenPressed(StopEverythingCommand())
    operatorController.Start.whenPressed(DiagnosticsTestCommand())
