from networktables import NetworkTables as nt

from subsystems.debuggablesubsystem import DebuggableSubsystem

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
from commands.drivetrain.gotocargoshipcommand import GoToCargoshipCommand
from commands.drivetrain.gotocargoshipcommandgroup import GoToCargoshipCommandGroup
#from commands.drivetrain.testgototapecommand import TestGoToTapeCommand
from commands.drivetrain.testgototapecommandgroup import TestGoToTapeCommandGroup

from commands.intake.intakecommand import IntakeCommand
from commands.intake.ejectcommand import EjectCommand
#from commands.intake.slowejectcommand import SlowEjectCommand
from commands.intake.intakeruncommand import IntakerunCommand

from commands.hatch.hatchejectcommand import HatchEjectCommand
from commands.hatch.hatchintakecommand import HatchIntakeCommand
from commands.hatch.slowejectcommand import SlowEjectCommand

from commands.elevator.elevatecommand import ElevateCommand
from commands.elevator.deelevatecommand import DeelevateCommand
from commands.elevator.panelejectcommand import PanelEjectCommand
from commands.elevator.resetelevatorcommand import ResetElevatorCommand
from commands.elevator.elevatorgotolevelcommand import ElevatorGoToLevelCommand
from commands.elevator.elevatorpidcommand import ElevatorPidCommand

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
from commands.arm.armpidcommand import ArmPidCommand

from commands.superstructure.superstructuregotolevelcommand import SuperStructureGoToLevelCommand
from commands.superstructure.upcommand import UpCommand
from commands.superstructure.downcommand import DownCommand
from commands.superstructure.superpidcommand import SuperPidCommand
from commands.superstructure.superpidlevel2command import SuperPidLevel2Command
from commands.superstructure.superpidlevel3command import SuperPidLevel3Command
from commands.superstructure.superballpidlevel1command import SuperBallPidLevel1Command
from commands.superstructure.superballpidlevel2command import SuperBallPidLevel2Command

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

from commands.togglelayoutcommand import ToggleLayoutCommand

#from commands.togglelayoutcommand import ToggleLayoutCommand

class Layout(DebuggableSubsystem):

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

        # TM Joysticks


    def init(self):
        from custom.config import Config

        selectedLayout = 1#Config('/DriveTrain/Layout', 0)

        if selectedLayout == 0:
            self.joystickOne = ThrustmasterJoystick(0)
            self.joystickTwo = ThrustmasterJoystick(1)

            logicalaxes.driveX = self.joystickOne.X
            logicalaxes.driveY = self.joystickOne.Y

            logicalaxes.driveRotate = self.joystickTwo.X


            #self.joystickOne.trigger.whileHeld(GoToTapeCommandGroup())
            #self.joystickOne.bottomThumb.whileHeld(GoPastTapeCommand())

            self.joystickOne.leftThumb.whenPressed(SlowEjectCommand())
            self.joystickOne.rightThumb.whileHeld(GoToCargoshipCommandGroup())

            self.joystickOne.Misc.whileHeld(RearRetractCommand())
            self.joystickOne.RightRightTop.whileHeld(AllRetractCommand())

            self.joystickOne.ClimbL3.whenPressed(lrAutoCommandGroup())
            self.joystickOne.ClimbL2.whenPressed(rrAutoCommandGroup())

            self.joystickOne.LeftRightTop.whenPressed(lrSecondAutoCommandGroup())
            self.joystickOne.RightLeftTop.whenPressed(rrSecondAutoCommandGroup())

            #self.joystickTwo.bottomThumb.whenPressed(ToggleFieldOrientationCommand())
            self.joystickTwo.leftThumb.whenPressed(ZeroGyroCommand())

            self.joystickTwo.rightThumb.whenPressed(HatchEjectCommand())
            self.joystickTwo.trigger.whenPressed(EjectCommand())

            self.joystickTwo.ClimbL3.whenPressed(L3ClimbCommandGroup())
            self.joystickTwo.ClimbL2.whenPressed(L2ClimbCommandGroup())

            self.joystickTwo.Misc.whileHeld(ResetCommand())
            self.joystickTwo.Layout.whenPressed(ToggleLayoutCommand())

            # The controller for non-driving subsystems of the robot
            self.controllerOne = LogitechDualShock(2)

            self.controllerOne.Back.whenPressed(ResetCommand())
            self.controllerOne.B.whenPressed(ZeroArmCommandGroup())

            self.controllerOne.LeftTrigger.whileHeld(LowerNoZeroCommand()) # Arm command
            self.controllerOne.LeftBumper.whileHeld(RaiseCommand()) # Arm command

            self.controllerOne.RightBumper.whileHeld(UpCommand()) # Superstructure command
            self.controllerOne.RightTrigger.whileHeld(DownCommand()) # Superstructure command

            self.controllerOne.X.whileHeld(DeelevateCommand())
            self.controllerOne.Y.whileHeld(ElevateCommand())

            self.controllerOne.DPadRight.whenPressed(ResetElevatorCommand())
            self.controllerOne.DPadUp.whenPressed(ElevatorGoToLevelCommand('cargoBalls'))
            self.controllerOne.DPadDown.whenPressed(SetArmCommandGroup(11.0))

            self.controllerOne.RightJoystick.toggleWhenPressed(IntakeCommand())
            self.controllerOne.LeftJoystick.toggleWhenPressed(HatchIntakeCommand())

        else:

            # The controller for driving the robot

            self.controllerOne = LogitechDualShock(0)

            logicalaxes.driveX = self.controllerOne.LeftX
            logicalaxes.driveY = self.controllerOne.LeftY
            logicalaxes.driveRotate = self.controllerOne.RightX

            self.controllerOne.LeftTrigger.whileHeld(GoToTapeCommandGroup())
            self.controllerOne.X.whileHeld(SuperPidLevel3Command())

            #self.controllerOne.Y.whenPressed(SuperPidCommand(56,50))
            #self.controllerOne.A.whenPressed(ToggleFieldOrientationCommand())
            self.controllerOne.RightTrigger.whenPressed(EjectCommand())
            self.controllerOne.B.whenPressed(HatchEjectCommand())

            self.controllerOne.Start.whenPressed(L3ClimbCommandGroup())
            self.controllerOne.Back.whenPressed(L2ClimbCommandGroup())

            self.controllerOne.RightJoystick.whenPressed(ToggleLayoutCommand())

            self.controllerOne.DPadDown.whileHeld(RearRetractCommand())
            self.controllerOne.A.whileHeld(SuperPidLevel2Command())


            # The self.controllerTwo for non-driving subsystems of the robot
            self.controllerTwo = LogitechDualShock(1)

            self.controllerTwo.Back.whenPressed(ResetCommand())
            self.controllerTwo.B.whenPressed(ZeroArmCommandGroup())
            #self.controllerTwo.A.whileHeld(TestGoToTapeCommandGroup())

            self.controllerTwo.LeftTrigger.whileHeld(LowerNoZeroCommand()) # Arm command
            self.controllerTwo.LeftBumper.whileHeld(RaiseCommand()) # Arm command

            self.controllerTwo.RightBumper.whileHeld(UpCommand()) # Superstructure command
            self.controllerTwo.RightTrigger.whileHeld(DownCommand()) # Superstructure command

            self.controllerTwo.X.whileHeld(DeelevateCommand())
            self.controllerTwo.Y.whileHeld(ElevateCommand())

            self.controllerTwo.DPadUp.whenPressed(SuperPidLevel3Command())
            self.controllerTwo.DPadRight.whenPressed((SuperPidLevel2Command()))
            self.controllerTwo.DPadDown.whenPressed(SuperBallPidLevel1Command())
            self.controllerTwo.Start.whileHeld(SuperBallPidLevel2Command())

            self.controllerTwo.RightJoystick.toggleWhenPressed(IntakeCommand())
            self.controllerTwo.LeftJoystick.toggleWhenPressed(HatchIntakeCommand())
