from .logitechdualshock import LogitechDualShock
from . import logicalaxes

from custom.config import Config

from commands.drive.drivecommand import DriveCommand
from commands.pickup.pickupcommand import PickupCommand
from commands.shooter.firecommand import FireCommand
from commands.gear.hanggearcommandgroup import HangGearCommandGroup
from commands.climber.climbcommand import ClimbCommand
from commands.gear.gearinbotcommand import GearInBotCommand

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
    mainController.RightTrigger.toggleWhenPressed(FireCommand(Config('Shooter/speed')))
    mainController.A.toggleWhenPressed(PickupCommand())
    mainController.LeftTrigger.toggleWhenPressed(ClimbCommand())
    mainController.LeftBumper.whenPressed(GearInBotCommand())

    backupController = LogitechDualShock(1)
