from .logitechdualshock import LogitechDualShock
from . import logicalaxes

from custom.config import Config

from commands.drive.drivecommand import DriveCommand
from commands.resetcommand import ResetCommand
from commands.pickup.pickupcommand import PickupCommand
from commands.shooter.firecommand import FireCommand
from commands.climber.climbcommand import ClimbCommand
from commands.gear.togglelightcommand import ToggleLightCommand
from commands.gear.scoregearcommand import ScoreGearCommand
from commands.printultrasonic import PrintUltrasonic

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

    mainController.LeftTrigger.toggleWhenPressed(ClimbCommand())
    mainController.RightTrigger.toggleWhenPressed(FireCommand(Config('Shooter/speed')))
    mainController.RightBumper.whenPressed(ScoreGearCommand())
    mainController.A.toggleWhenPressed(PickupCommand())
    mainController.B.whenPressed(ToggleLightCommand())
    mainController.X.toggleWhenPressed(DriveCommand(Config('DriveTrain/preciseSpeed')))
    mainController.Y.whenPressed(PrintUltrasonic())
    mainController.Back.whenPressed(ResetCommand())


    backupController = LogitechDualShock(1)

    backupController.LeftTrigger.toggleWhenPressed(ClimbCommand())
    backupController.RightTrigger.toggleWhenPressed(FireCommand(Config('Shooter/speed')))
    backupController.RightBumper.whenPressed(ScoreGearCommand())
    backupController.A.toggleWhenPressed(PickupCommand())
    backupController.B.whenPressed(ToggleLightCommand())
