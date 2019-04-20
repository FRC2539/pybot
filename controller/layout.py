from networktables import NetworkTables as nt

from .logitechdualshock import LogitechDualShock
from .logitechjoystick import LogitechJoystick
from .thrustmasterjoystick import ThrustmasterJoystick

from . import logicalaxes

from custom.config import Config

from commands.resetcommand import ResetCommand

from commands.drivetrain.drivecommand import DriveCommand

from commands.rrautocommandgroup import rrAutoCommandGroup
from commands.lrautocommandgroup import lrAutoCommandGroup

from commands.rrsecondautocommandgroup import rrSecondAutoCommandGroup
from commands.lrsecondautocommandgroup import lrSecondAutoCommandGroup


from commands.drivetrain.zerogyrocommand import ZeroGyroCommand
from commands.drivetrain.togglefieldorientationcommand import ToggleFieldOrientationCommand
from commands.drivetrain.holonomicmovecommand import HolonomicMoveCommand
from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.strafecommand import StrafeCommand
from commands.drivetrain.gototapecommand import GoToTapeCommand
from commands.drivetrain.gototapecommandgroup import GoToTapeCommandGroup
from commands.drivetrain.gopasttapecommand import GoPastTapeCommand
from commands.drivetrain.autonomousmeasurecommand import AutonomousMeasureCommand

from commands.intake.intakecommand import IntakeCommand
from commands.intake.ejectcommand import EjectCommand
from commands.intake.slowejectcommand import SlowEjectCommand

from commands.hatch.hatchejectcommand import HatchEjectCommand
from commands.hatch.hatchintakecommand import HatchIntakeCommand

from commands.elevator.elevatecommand import ElevateCommand
from commands.elevator.deelevatecommand import DeelevateCommand
from commands.elevator.panelejectcommand import PanelEjectCommand

from commands.arm.raisecommand import RaiseCommand
from commands.arm.lowercommand import LowerCommand
from commands.arm.lowernozerocommand import LowerNoZeroCommand
from commands.arm.forcelowercommand import ForceLowerCommand
from commands.arm.forceraisecommand import ForceRaiseCommand
from commands.arm.grabhatchcommand import GrabHatchCommand
from commands.arm.upstagecommand import UpStageCommand
from commands.arm.downstagecommand import DownStageCommand
from commands.arm.setarmcommandgroup import SetArmCommandGroup
from commands.arm.zeroarmcommandgroup import ZeroArmCommandGroup

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

    #if driveLayoutPrimary:

    # The joysticks for driving the robot
    """
    driveStick = LogitechJoystick(0)
    rotateStick = LogitechJoystick(1)

    logicalaxes.driveX = driveStick.X
    logicalaxes.driveY = driveStick.Y
    logicalaxes.driveRotate = rotateStick.X

    driveStick.trigger.whileHeld(GoToTapeCommand())
    driveStick.bottomThumb.whileHeld(GoPastTapeCommand())

    rotateStick.topThumb.whenPressed(ZeroGyroCommand())
    rotateStick.bottomThumb.whenPressed(ToggleFieldOrientationCommand())
    rotateStick.trigger.whenPressed(EjectCommand())

    rotateStick.Button8.whenPressed(L3ClimbCommandGroup())
    rotateStick.Button9.whenPressed(L2ClimbCommandGroup())


    controller = LogitechDualShock(2)

    controller.Back.whenPressed(ResetCommand())


    controller.LeftTrigger.whileHeld(LowerCommand()) # Arm command
    controller.LeftBumper.whileHeld(RaiseCommand()) # Arm command

    controller.RightBumper.whileHeld(UpCommand()) # Superstructure command
    controller.RightTrigger.whileHeld(DownCommand()) # Superstructure command

    controller.A.whenPressed(SuperStructureGoToLevelCommand('floor'))
    controller.B.whenPressed(SuperStructureGoToLevelCommand('midHatches'))


    controller.X.whileHeld(DeelevateCommand())
    controller.Y.whileHeld(ElevateCommand())

    controller.RightJoystick.toggleWhenPressed(IntakeCommand())
    controller.LeftJoystick.whenPressed(StrafeCommand(-36))



    else:
    """
    backupDriveStick = ThrustmasterJoystick(0)
    backupRotateStick = ThrustmasterJoystick(1)

    logicalaxes.driveX = backupDriveStick.X
    logicalaxes.driveY = backupDriveStick.Y

    logicalaxes.driveRotate = backupRotateStick.X

    backupDriveStick.trigger.whileHeld(GoToTapeCommandGroup())
    backupDriveStick.bottomThumb.whileHeld(GoPastTapeCommand())

    backupDriveStick.Misc.whileHeld(RearRetractCommand())

    backupDriveStick.ClimbL3.whenPressed(lrAutoCommandGroup())
    backupDriveStick.ClimbL2.whenPressed(rrAutoCommandGroup())

    backupDriveStick.LeftRightTop.whenPressed(lrSecondAutoCommandGroup())
    backupDriveStick.RightLeftTop.whenPressed(rrSecondAutoCommandGroup())

    backupRotateStick.bottomThumb.whenPressed(ToggleFieldOrientationCommand())
    backupRotateStick.leftThumb.whenPressed(ZeroGyroCommand())

    backupRotateStick.rightThumb.whenPressed(HatchEjectCommand())
    backupRotateStick.trigger.whenPressed(EjectCommand())


    backupRotateStick.ClimbL3.whenPressed(L3ClimbCommandGroup())
    backupRotateStick.ClimbL2.whenPressed(L2ClimbCommandGroup())

    backupRotateStick.Misc.whileHeld(ResetCommand())

    # The controller for non-driving subsystems of the robot
    controller = LogitechDualShock(2)

    controller.Back.whenPressed(ResetCommand())
    controller.B.whenPressed(ZeroArmCommandGroup())

    controller.LeftTrigger.whileHeld(LowerNoZeroCommand()) # Arm command
    controller.LeftBumper.whileHeld(RaiseCommand()) # Arm command

    controller.RightBumper.whileHeld(UpCommand()) # Superstructure command
    controller.RightTrigger.whileHeld(DownCommand()) # Superstructure command

    controller.X.whileHeld(DeelevateCommand())
    controller.Y.whileHeld(ElevateCommand())

    controller.DPadUp.whenPressed(SetArmCommandGroup(70.0, 20.0))
    controller.DPadDown.whenPressed(SetArmCommandGroup(11.0))

    controller.RightJoystick.toggleWhenPressed(IntakeCommand())
    controller.LeftJoystick.toggleWhenPressed(HatchIntakeCommand())
