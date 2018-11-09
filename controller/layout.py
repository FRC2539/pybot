from .logitechdualshock import LogitechDualShock
from . import logicalaxes

from custom.config import Config

from commands.drivetrain.drivecommand import DriveCommand
from commands.resetcommand import ResetCommand
from commands.elevator.slowlowercommand import SlowLowerCommand
from commands.elevator.lowerballcommand import LowerBallCommand
from commands.elevator.raiseballcommand import RaiseBallCommand
from commands.elevator.slowraisecommand import SlowRaiseCommand
from commands.indexwheel.indexreversecommand import IndexReverseCommand
from commands.indexwheel.indexforwardcommand import IndexForwardCommand
from commands.indexwheel.indexslowforwardcommand import IndexSlowForwardCommand
from commands.shooter.shootcommand import ShootCommand
from commands.shooter.slowshootcommand import SlowShootCommand
from commands.shooter.shootercommandgroup import ShooterCommandGroup
from commands.shooter.vspeedshootcommandgroup import VariedSpeedShootCommandGroup
from commands.shooter.increasefirespeedcommand import IncreaseFireSpeedCommand
from commands.shooter.decreasefirespeedcommand import DecreaseFireSpeedCommand


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
    driveController.LeftTrigger.toggleWhenPressed(VariedSpeedShootCommandGroup())
    driveController.LeftBumper.whileHeld(LowerBallCommand())
    driveController.RightTrigger.toggleWhenPressed(ShooterCommandGroup())
    driveController.RightBumper.whileHeld(RaiseBallCommand())
    driveController.A.whileHeld(IndexForwardCommand())
    driveController.DPadUp.whenPressed(IncreaseFireSpeedCommand())
    driveController.DPadDown.whenPressed(DecreaseFireSpeedCommand())

    #driveController.DPadLeft.toggleWhenPressed(SlowShootCommand())

    # The controller for non-driving subsystems of the robot
    componentController = LogitechDualShock(1)

    componentController.Back.whenPressed(ResetCommand())
    componentController.LeftTrigger.toggleWhenPressed(VariedSpeedShootCommandGroup())
    componentController.LeftBumper.whileHeld(LowerBallCommand())
    componentController.RightTrigger.toggleWhenPressed(ShooterCommandGroup())
    componentController.RightBumper.whileHeld(RaiseBallCommand())
    componentController.A.whileHeld(IndexForwardCommand())
    componentController.DPadUp.whenPressed(IncreaseFireSpeedCommand())
    componentController.DPadDown.whenPressed(DecreaseFireSpeedCommand())
