from .logitechdualshock import LogitechDualShock
from thrustmasterjoystick import ThrustmasterJoystick
from . import logicalaxes

from custom.config import Config

from commands.drivetrain.drivecommand import DriveCommand
from commands.drivetrain.togglefieldorientationcommand import ToggleFieldOrientationCommand

from commands.resetcommand import ResetCommand


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
    driveControllerOne = ThrustmasterJoystick(0) # The left hand controller
    driveControllerTwo = ThrustmasterJoystick(1) # The right hand controller

    logicalaxes.forward = driveControllerOne.Y
    logicalaxes.strafe = driveControllerOne.X
    logicalaxes.rotate = driveControllerTwo.X

    driveControllerOne.Back.whenPressed(ResetCommand())
    driveControllerOne.RightThumb.whenPressed(ToggleFieldOrientationCommand())

    # The controller for non-driving subsystems of the robot
    componentController = LogitechDualShock(1)

    componentController.Back.whenPressed(ResetCommand())
