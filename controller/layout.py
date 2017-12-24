from .logitechdualshock import LogitechDualShock
from . import logicalaxes

from commands.lights.oncommand import OnCommand

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

    mainController = LogitechDualShock(0)

    logicalaxes.driveX = mainController.LeftX
    logicalaxes.driveY = mainController.LeftY
    logicalaxes.driveRotate = mainController.RightX

    mainController.A.toggleWhenPressed(OnCommand(0))
    mainController.B.toggleWhenPressed(OnCommand(1))
    mainController.X.toggleWhenPressed(OnCommand(2))
