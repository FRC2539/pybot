from .logitechdualshock import LogitechDualShock
from . import logicalaxes

from .logitechjoystick import LogitechJoystick

from custom.config import Config

from commands.drivetrain.drivecommand import DriveCommand
from commands.resetcommand import ResetCommand
from commands.drivetrain.zerogyrocommand import ZeroGyroCommand
from commands.drivetrain.togglefieldorientationcommand import ToggleFieldOrientationCommand

from commands.lights.orangelightscommand import OrangeLightsCommand
from commands.lights.lightsoffcommand import LightsOffCommand
from commands.lights.teamcolorlightscommand import TeamColorLightsCommand
from commands.lights.seizurelightscommand import SeizureLightsCommand

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

    # The joysticks for driving the robot
    driveStick = LogitechJoystick(0)
    rotateStick = LogitechJoystick(1)

    logicalaxes.driveX = driveStick.X
    logicalaxes.driveY = driveStick.Y
    logicalaxes.driveRotate = rotateStick.X


    rotateStick.topThumb.whenPressed(ZeroGyroCommand())
    rotateStick.bottomThumb.whenPressed(ToggleFieldOrientationCommand())

    # The controller for non-driving subsystems of the robot
    controller = LogitechDualShock(2)

    controller.Back.whenPressed(ResetCommand())
    controller.A.toggleWhenPressed(TeamColorLightsCommand())
    controller.B.toggleWhenPressed(SeizureLightsCommand())
    controller.X.toggleWhenPressed(LightsOffCommand())
    controller.Y.whileHeld(OrangeLightsCommand())
