from .logitechdualshock import LogitechDualShock
from . import logicalaxes

from custom.config import Config

from commands.resetcommand import ResetCommand

from commands.drivetrain.drivecommand import DriveCommand
from commands.drivetrain.arcfollowercommand import ArcFollowerCommand

from commands.revolver.shooterdirectioncommand import ShooterDirectionCommand
from commands.revolver.intakedirectioncommand import IntakeDirectionCommand
from commands.revolver.advancedmovecommand import AdvancedMoveCommand

from commands.balllauncher.launchballscommand import LaunchBallsCommand
from commands.balllauncher.reverseballscommand import ReverseBallsCommand
from commands.balllauncher.extendlaunchercommand import ExtendLauncherCommand

from commands.intake.intakecommand import IntakeCommand
from commands.intake.outakecommand import OutakeCommand
from commands.intake.kickcommand import KickCommand
from commands.intake.loadinemptycommandgroup import LoadInEmptyCommandGroup

from commands.hood.raisehoodcommand import RaiseHoodCommand
from commands.hood.lowerhoodcommand import LowerHoodCommand

from commands.limelight.sudocommandgroup import SudoCommandGroup

from commands.shooter.shootwhenreadycommand import ShootWhenReadyCommand
from commands.shooter.endshootingprocesscommand import EndShootingProcessCommand
from commands.shooter.setrpmcommand import SetRPMCommand

from commands.turret.toggleturretmodecommand import ToggleTurretModeCommand

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

    operatorController = LogitechDualShock(1)

    logicalaxes.driveX = driveController.LeftX
    logicalaxes.driveY = driveController.LeftY
    logicalaxes.driveRotate = driveController.RightX
    logicalaxes.speedControl = driveController.RightY

    logicalaxes.turretX = operatorController.RightX

    driveController.Back.whenPressed(ResetCommand())

    driveController.A.toggleWhenPressed(ShooterDirectionCommand(
))
    driveController.B.toggleWhenPressed(IntakeDirectionCommand())
    driveController.X.toggleWhenPressed(LaunchBallsCommand())
    driveController.Y.toggleWhenPressed(ReverseBallsCommand())

    driveController.DPadUp.toggleWhenPressed(ShootWhenReadyCommand())
    driveController.DPadDown.toggleWhenPressed(LoadInEmptyCommandGroup())
    driveController.DPadRight.toggleWhenPressed(SudoCommandGroup())
    driveController.DPadLeft.toggleWhenPressed(SetRPMCommand(3500))

    driveController.RightBumper.toggleWhenPressed(ExtendLauncherCommand())
    driveController.RightTrigger.toggleWhenPressed(SetRPMCommand(4500))

    driveController.LeftBumper.whileHeld(RaiseHoodCommand())
    driveController.LeftTrigger.whileHeld(LowerHoodCommand())

    driveController.RightJoystick.toggleWhenPressed(IntakeCommand())
    driveController.LeftJoystick.toggleWhenPressed(OutakeCommand())

    driveController.Start.toggleWhenPressed(ArcFollowerCommand(8, 90, True))

    # The controller for non-driving subsystems of the robot
    # actually just the driver controller but some stuff is switched (A and B, left trigger and bumper) and a command is gone

    operatorController.Start.whenPressed(EndShootingProcessCommand())
    operatorController.Back.whenPressed(ToggleTurretModeCommand())

    operatorController.A.toggleWhenPressed(IntakeDirectionCommand())
    operatorController.B.toggleWhenPressed(ShooterDirectionCommand())
    operatorController.X.toggleWhenPressed(LaunchBallsCommand())
    operatorController.Y.toggleWhenPressed(ReverseBallsCommand())

    operatorController.DPadUp.toggleWhenPressed(ExtendLauncherCommand())
    operatorController.DPadDown.toggleWhenPressed(LoadInEmptyCommandGroup())
    operatorController.DPadRight.toggleWhenPressed(SudoCommandGroup())

    operatorController.RightTrigger.toggleWhenPressed(ShootWhenReadyCommand())
    operatorController.RightBumper.toggleWhenPressed(SetRPMCommand(3500))

    operatorController.LeftTrigger.whileHeld(RaiseHoodCommand())
    operatorController.LeftBumper.whileHeld(LowerHoodCommand())

    operatorController.LeftJoystick.toggleWhenPressed(OutakeCommand())
