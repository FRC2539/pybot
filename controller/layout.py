from .logitechdualshock import LogitechDualShock
from . import logicalaxes

from custom.config import Config

from commands.drivetrain.drivecommand import DriveCommand
from commands.resetcommand import ResetCommand

from commands.intake.intakecommand import IntakeCommand
from commands.intake.outtakecommand import OutakeCommand

from commands.colorwheel.getcolorcommand import GetColorCommand

from commands.turret.turretmovecommand import turretMoveCommand

from commands.ballsystem.runallcommand import RunAllCommand
from commands.ballsystem.runindexwithverticalcommand import RunIndexWithVerticalCommand
from commands.ballsystem.runlowercommand import RunLowerCommand

from commands.pneumaticsystems.runcompressor import RunCompressorCommand

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

    driveController.Start.toggleWhenPressed(RunCompressorCommand())

    # The controller for non-driving subsystems of the robot
    operatorController = LogitechDualShock(1)

    logicalaxes.operatorX = operatorController.RightX

    operatorController.A.whileHeld(IntakeCommand(0.5))# variable speed, 100% is default

    operatorController.X.toggleWhenPressed(RunAllCommand())
    operatorController.Y.toggleWhenPressed(RunIndexWithVerticalCommand())
    operatorController.B.toggleWhenPressed(RunLowerCommand())

    operatorController.Back.whenPressed(ResetCommand())
