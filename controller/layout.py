from .logitechdualshock import LogitechDualShock
from . import logicalaxes

from custom.config import Config

from commands.drivetrain.drivecommand import DriveCommand
from commands.resetcommand import ResetCommand

from commands.pneumatics.intakeaircommand import IntakeAirCommand
from commands.pneumatics.stopintakecommand import StopIntakeCommand

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
    driveController.X.toggleWhenPressed(DriveCommand(Config('DriveTrain/preciseSpeed')))

    driveController.A.whenPressed(IntakeAirCommand()) # Should stop by itself.
    driveController.B.whenPressed(StopIntakeCommand())

    # The controller for non-driving subsystems of the robot
    componentController = LogitechDualShock(1)

    componentController.Back.whenPressed(ResetCommand())
