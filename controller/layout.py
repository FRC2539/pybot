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
    driveController.LeftTrigger.whileHeld(SlowLowerCommand())
    driveController.LeftBumper.whileHeld(LowerBallCommand())
    driveController.RightTrigger.whileHeld(SlowRaiseCommand())
    driveController.RightBumper.whileHeld(RaiseBallCommand())
    driveController.Y.whileHeld(IndexReverseCommand())
    driveController.A.whileHeld(IndexForwardCommand())
    driveController.B.whileHeld(IndexSlowForwardCommand())
    driveController.X.whileHeld(ShootCommand())
    driveController.DPadLeft.toggleWhenPressed(SlowShootCommand())

    # The controller for non-driving subsystems of the robot
    componentController = LogitechDualShock(1)

    componentController.Back.whenPressed(ResetCommand())
    componentController.LeftTrigger.whileHeld(SlowLowerCommand())
    componentController.LeftBumper.whileHeld(LowerBallCommand())
    componentController.RightTrigger.whileHeld(SlowRaiseCommand())
    componentController.RightBumper.whileHeld(RaiseBallCommand())
    componentController.Y.whileHeld(IndexReverseCommand())
    componentController.A.whileHeld(IndexForwardCommand())
    componentController.B.whileHeld(IndexSlowForwardCommand())
    componentController.X.toggleWhenPressed(ShootCommand())
    componentController.DPadLeft.toggleWhenPressed(SlowShootCommand())
