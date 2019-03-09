from .logitechdualshock import LogitechDualShock
from .logitechjoystick import LogitechJoystick
from . import logicalaxes

from custom.config import Config

from commands.resetcommand import ResetCommand

from commands.drivetrain.drivecommand import DriveCommand

from commands.drivetrain.zerogyrocommand import ZeroGyroCommand
from commands.drivetrain.togglefieldorientationcommand import ToggleFieldOrientationCommand
from commands.drivetrain.holonomicmovecommand import HolonomicMoveCommand
from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.gototapecommand import GoToTapeCommand

from commands.intake.intakecommand import IntakeCommand
from commands.intake.ejectcommand import EjectCommand
from commands.intake.slowejectcommand import SlowEjectCommand

from commands.elevator.elevatecommand import ElevateCommand
from commands.elevator.deelevatecommand import DeelevateCommand
from commands.elevator.panelejectcommand import PanelEjectCommand

from commands.arm.raisecommand import RaiseCommand
from commands.arm.lowercommand import LowerCommand
from commands.arm.forcelowercommand import ForceLowerCommand
from commands.arm.forceraisecommand import ForceRaiseCommand

from commands.superstructure.superstructuregotolevelcommand import SuperStructureGoToLevelCommand
from commands.superstructure.upcommand import UpCommand
from commands.superstructure.downcommand import DownCommand

from commands.climber.allextendcommand import AllExtendCommand
from commands.climber.allretractcommand import AllRetractCommand
from commands.climber.frontretractcommand import FrontRetractCommand
from commands.climber.rearretractcommand import RearRetractCommand
from commands.climber.rightretractcommand import RightRetractCommand
from commands.climber.leftretractcommand import LeftRetractCommand
from commands.climber.extendleftcommand import ExtendLeftCommand
from commands.climber.extendrightcommand import ExtendRightCommand
from commands.climber.extendrearcommand import ExtendRearCommand
from commands.climber.driveforwardcommand import DriveForwardCommand
from commands.climber.drivebackwardcommand import DriveBackwardCommand
from commands.climber.l3climbcommandgroup import L3ClimbCommandGroup
from commands.climber.l2climbcommandgroup import L2ClimbCommandGroup

from commands.lights.orangelightscommand import OrangeLightsCommand
from commands.lights.seizurelightscommand import SeizureLightsCommand
from commands.lights.lightsoffcommand import LightsOffCommand
from commands.lights.visionbasedlightscommand import VisionBasedLightsCommand


def init():
    driveLayoutPrimary = Config('DriveTrain/Layout', True)

    '''
    Declare all controllers, assign axes to logical axes, and trigger
    commands on various button events. Available event types are:
        - whenPressed
        - whileHeld: cancelled when the button is released
        - whenReleased
        - toggleWhenPressed: sta
        rt on first press, cancel on next
        - cancelWhenPressed: good for commands started with a different button
    '''

    # The joysticks for driving the robot
    if driveLayoutPrimary:

        driveStick = LogitechJoystick(0)
        rotateStick = LogitechJoystick(1)

        logicalaxes.driveX = driveStick.X
        logicalaxes.driveY = driveStick.Y
        logicalaxes.driveRotate = rotateStick.X

        driveStick.trigger.whileHeld(GoToTapeCommand())

        rotateStick.topThumb.whenPressed(ZeroGyroCommand())
        rotateStick.bottomThumb.whenPressed(ToggleFieldOrientationCommand())
        rotateStick.trigger.whenPressed(EjectCommand())

        rotateStick.Button8.whenPressed(L3ClimbCommandGroup())
        rotateStick.Button9.whenPressed(L2ClimbCommandGroup())

        rotateStick.Button10.whileHeld(ForceLowerCommand())


        controller = LogitechDualShock(2)

        controller.Back.whenPressed(ResetCommand())
        controller.Start.whenPressed(ForceLowerCommand())

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

        '''
        controller.A.whenPressed(SuperStructureGoToLevelCommand('floor'))
        controller.X.whenPressed(SuperStructureGoToLevelCommand('aboveFloor'))
        '''
        controller.B.whenPressed(SuperStructureGoToLevelCommand('lowHatches'))
        #controller.B.whenPressed(SuperStructureGoToLevelCommand('highHatches'))


        #controller.A.toggleWhenPressed(IntakeCommand())
        #controller.B.whenPressed(SlowEjectCommand())

        controller.X.whileHeld(DeelevateCommand())
        controller.Y.whileHeld(ElevateCommand())


        controller.RightJoystick.toggleWhenPressed(IntakeCommand())
        #controller.LeftJoystick.whenPressed(EjectCommand())



    else:
        driveController = LogitechDualShock(0)

        logicalaxes.driveX = driveController.LeftX
        logicalaxes.driveY = driveController.LeftY

        logicalaxes.driveRotate = driveController.RightX

        driveController.A.whenPressed(ZeroGyroCommand())
        driveController.X.whenPressed(ToggleFieldOrientationCommand())
        driveController.B.whileHeld(ForceLowerCommand())
        driveController.RightTrigger.whenPressed(EjectCommand())

        driveController.DPadUp.whenPressed(L3ClimbCommandGroup())
        driveController.DPadDown.whenPressed(L2ClimbCommandGroup())
    # The controller for non-driving subsystems of the robot


        controller = LogitechDualShock(1)

        controller.Back.whenPressed(ResetCommand())
        controller.Start.whenPressed(ForceLowerCommand())

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

        '''
        controller.A.whenPressed(SuperStructureGoToLevelCommand('floor'))
        controller.X.whenPressed(SuperStructureGoToLevelCommand('aboveFloor'))
        controller.Y.whenPressed(SuperStructureGoToLevelCommand('midHatches'))
        controller.B.whenPressed(SuperStructureGoToLevelCommand('highHatches'))
        '''

        #controller.A.toggleWhenPressed(IntakeCommand())
        #controller.B.whenPressed(SlowEjectCommand())

        controller.X.whileHeld(DeelevateCommand())
        controller.Y.whileHeld(ElevateCommand())


        controller.RightJoystick.toggleWhenPressed(IntakeCommand())
        #controller.LeftJoystick.whenPressed(EjectCommand())
