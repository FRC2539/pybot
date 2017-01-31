from .logitechdualshock import LogitechDualShock
from . import logicalaxes

from custom.config import Config

from commands.drivecommand import DriveCommand
from commands.shootercommand import ShooterCommand
from commands.pickupcommand import PickupCommand
from commands.autonomous.movecommand import MoveCommand
from commands.autonomous.turncommand import TurnCommand

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

    mainController.X.toggleWhenPressed(DriveCommand(Config('DriveTrain/preciseSpeed')))
    mainController.Y.whenPressed(MoveCommand(24))
    mainController.B.toggleWhenPressed(ShooterCommand(Config('Shooter/speed')))
    mainController.A.toggleWhenPressed(PickupCommand())

    backupController = LogitechDualShock(1)
