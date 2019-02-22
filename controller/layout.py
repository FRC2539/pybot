from .logitechdualshock import LogitechDualShock
from . import logicalaxes

from .logitechjoystick import LogitechJoystick

from custom.config import Config

from commands.drivetrain.drivecommand import DriveCommand
from commands.resetcommand import ResetCommand
from commands.drivetrain.zerogyrocommand import ZeroGyroCommand
from commands.drivetrain.togglefieldorientationcommand import ToggleFieldOrientationCommand
from commands.drivetrain.holonomicmovecommand import HolonomicMoveCommand
from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.donutscommand import DonutsCommand

from commands.intake.intakecommand import IntakeCommand
from commands.intake.ejectcommand import EjectCommand
from commands.intake.slowejectcommand import SlowEjectCommand

from commands.elevator.elevatecommand import ElevateCommand
from commands.elevator.deelevatecommand import DeelevateCommand
from commands.elevator.panelejectcommand import PanelEjectCommand

from commands.arm.raisecommand import RaiseCommand
from commands.arm.lowercommand import LowerCommand

from commands.superstructure.upcommand import UpCommand
from commands.superstructure.downcommand import DownCommand

from commands.climber.allextendcommand import AllExtendCommand
from commands.climber.allretractcommand import AllRetractCommand
from commands.climber.frontretractcommand import FrontRetractCommand
from commands.climber.rearretractcommand import RearRetractCommand
from commands.climber.driveforwardcommand import DriveForwardCommand
from commands.climber.drivebackwardcommand import DriveBackwardCommand
from commands.climber.climbcommandgroup import ClimbCommandGroup

from commands.lights.firelightscommand import FireLightsCommand
from commands.lights.orangelightscommand import OrangeLightsCommand
from commands.lights.teamcolorlightscommand import TeamColorLightsCommand
from commands.lights.seizurelightscommand import SeizureLightsCommand
from commands.lights.lightsoffcommand import LightsOffCommand


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

    logicalaxes.climb = rotateStick.bottomThing

    driveStick.trigger.toggleWhenPressed(IntakeCommand())

    rotateStick.topThumb.whenPressed(ZeroGyroCommand())
    rotateStick.bottomThumb.whenPressed(ToggleFieldOrientationCommand())
    rotateStick.trigger.whenPressed(EjectCommand())

    rotateStick.Button8.whenPressed(ClimbCommandGroup())

    #rotateStick.Button6.whenPressed(HolonomicMoveCommand(70, 54, 45))

    # The controller for non-driving subsystems of the robot
    controller = LogitechDualShock(2)

    controller.Back.whenPressed(ResetCommand())

    """
    controller.RightBumper.whileHeld(AllExtendCommand())
    controller.RightTrigger.whileHeld(AllRetractCommand())

    controller.A.whileHeld(DriveForwardCommand())
    controller.B.whileHeld(DriveBackwardCommand())
    controller.X.whileHeld(FrontRetractCommand())
    controller.Y.whileHeld(RearRetractCommand())
    """

    controller.LeftTrigger.whileHeld(LowerCommand()) # Arm command
    controller.LeftBumper.whileHeld(RaiseCommand()) # Arm command

    controller.RightBumper.whileHeld(UpCommand()) # Superstructure command
    controller.RightTrigger.whileHeld(DownCommand()) # Superstructure command

    controller.A.toggleWhenPressed(IntakeCommand())
    controller.B.whenPressed(EjectCommand())
    controller.DPadRight.whenPressed(SlowEjectCommand())

    controller.X.whileHeld(DeelevateCommand()) # Elevator command
    controller.Y.whileHeld(ElevateCommand()) # Elevator command
    controller.DPadLeft.whenPressed(PanelEjectCommand()) # Lower the elevator slightly, just to removed the hatch panel.
