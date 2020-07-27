from .logitechdualshock import LogitechDualShock
from . import logicalaxes

from custom.config import Config

from commands.drivetrain.drivecommand import DriveCommand
from commands.resetcommand import ResetCommand

from commands.revolver.shooterdirectioncommand import ShooterDirectionCommand
from commands.revolver.intakedirectioncommand import IntakeDirectionCommand

from commands.balllauncher.launchballscommand import LaunchBallsCommand
from commands.balllauncher.reverseballscommand import ReverseBallsCommand
from commands.balllauncher.extendlaunchercommand import ExtendLauncherCommand

from commands.shooter.spitballscommand import SpitBallsCommand

from commands.intake.intakecommand import IntakeCommand
from commands.intake.outakecommand import OutakeCommand
from commands.intake.kickcommand import KickCommand

from commands.hood.raisehoodcommand import RaiseHoodCommand
from commands.hood.lowerhoodcommand import LowerHoodCommand

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
    logicalaxes.speedControl = driveController.RightY

    driveController.Back.whenPressed(ResetCommand())

    driveController.A.toggleWhenPressed(ShooterDirectionCommand())
    driveController.B.toggleWhenPressed(IntakeDirectionCommand())

    driveController.X.toggleWhenPressed(LaunchBallsCommand())
    driveController.Y.toggleWhenPressed(ReverseBallsCommand())

    driveController.RightBumper.toggleWhenPressed(ExtendLauncherCommand())

    driveController.RightTrigger.toggleWhenPressed(SpitBallsCommand())

    driveController.LeftBumper.whileHeld(RaiseHoodCommand())
    driveController.LeftTrigger.whileHeld(LowerHoodCommand())

    # The controller for non-driving subsystems of the robot
    componentController = LogitechDualShock(1)

    componentController.Back.whenPressed(ResetCommand())
