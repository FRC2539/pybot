from .logitechdualshock import LogitechDualShock
from . import logicalaxes

from custom.config import Config

from commands.drivetrain.drivecommand import DriveCommand
from commands.resetcommand import ResetCommand

from commands.intake.intakecommand import IntakeCommand
from commands.intake.outtakecommand import OutakeCommand
from commands.intake.clearjamtwocommand import ClearJamTwoCommand

from commands.colorwheel.getcolorcommand import GetColorCommand

from commands.turret.turretmovecommand import turretMoveCommand

from commands.ballsystem.runallcommand import RunAllCommand
from commands.ballsystem.runindexwithverticalcommand import RunIndexWithVerticalCommand
from commands.ballsystem.runlowercommand import RunLowerCommand

from commands.ballsystem.reversehorizontalcommand import ReverseHorizontalCommand
from commands.ballsystem.clearjamcommand import ClearJamCommand

from commands.ballsystem.runballflowcommandgroup import RunBallFlowCommandGroup

from commands.pneumaticsystems.runcompressor import RunCompressorCommand

from commands.hood.raisehoodcommand import RaiseHoodCommand
from commands.hood.lowerhoodcommand import LowerHoodCommand
from commands.hood.sethoodcommand import SetHoodCommand

from commands.shooter.shootcommand import ShootCommand
from commands.shooter.controlledshootcommand import ControlledShootCommand

from commands.pneumaticsystems.extendclimberpistoncommand import ExtendClimberPistonCommand

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

    driveController.A.toggleWhenPressed(IntakeCommand())
    driveController.X.whenPressed(GetColorCommand())
    driveController.B.whenPressed(OutakeCommand())

    driveController.Y.toggleWhenPressed(ExtendClimberPistonCommand())

    driveController.RightBumper.whileHeld(RaiseHoodCommand())
    driveController.RightTrigger.whileHeld(LowerHoodCommand())

    driveController.Start.toggleWhenPressed(RunCompressorCommand())

    driveController.LeftBumper.toggleWhenPressed(SetHoodCommand(140))

    # The controller for non-driving subsystems of the robot
    operatorController = LogitechDualShock(1)

    logicalaxes.operatorX = operatorController.RightX

    operatorController.A.toggleWhenPressed(RunBallFlowCommandGroup())# variable speed, 100% is default

    operatorController.X.toggleWhenPressed(ClearJamTwoCommand())
    operatorController.Y.toggleWhenPressed(ReverseHorizontalCommand())
    operatorController.B.toggleWhenPressed(ClearJamCommand())

    operatorController.RightBumper.whileHeld(RaiseHoodCommand())
    operatorController.RightTrigger.whileHeld(LowerHoodCommand())

    operatorController.LeftTrigger.toggleWhenPressed(ShootCommand())
    operatorController.LeftBumper.toggleWhenPressed(ControlledShootCommand(2850))

    operatorController.Back.whenPressed(ResetCommand())
