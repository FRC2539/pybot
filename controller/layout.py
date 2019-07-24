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

from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.gototapecommand import GoToTapeCommand
from commands.drivetrain.gototapecommandgroup import GoToTapeCommandGroup
from commands.drivetrain.gopasttapecommand import GoPastTapeCommand
from commands.drivetrain.autonomousmeasurecommand import AutonomousMeasureCommand
from commands.drivetrain.togglespeedcommand import ToggleSpeedCommand

from commands.intake.intakecommand import IntakeCommand
from commands.intake.ejectcommand import EjectCommand
from commands.intake.slowejectcommand import SlowEjectCommand

from commands.elevator.elevatecommand import ElevateCommand
from commands.elevator.deelevatecommand import DeelevateCommand
from commands.elevator.elevatorgotolevelcommand import ElevatorGoToLevelCommand
from commands.elevator.forcelowercommand import ForceLowerCommand

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
from commands.climber.doubleclimbcommand import DoubleClimbCommand
from commands.climber.holdupcommandgroup import HoldUpCommandGroup

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

        selectedLayout = 1#Config('/DriveTrain/Layout', 1)

        if selectedLayout == 0:
            self.joystickOne = ThrustmasterJoystick(0)
            self.joystickTwo = ThrustmasterJoystick(1)

            logicalaxes.driveX = self.joystickOne.X
            logicalaxes.driveY = self.joystickOne.Y

            logicalaxes.driveRotate = self.joystickTwo.X

            self.joystickOne.trigger.whileHeld(GoToTapeCommandGroup())
            self.joystickOne.bottomThumb.whileHeld(GoPastTapeCommand())

            self.joystickOne.Misc.whenPressed(AllRetractCommand())

            self.joystickOne.LeftRightTop.whenPressed(lrSecondAutoCommandGroup())

            self.joystickOne.ClimbL3.whenPressed(lrAutoCommandGroup())
            self.joystickOne.LeftMiddleTop.whenPressed(rrAutoCommandGroup())

            self.joystickOne.LeftLeftBottom.whenPressed(rrSecondAutoCommandGroup())

            self.joystickTwo.trigger.whenPressed(EjectCommand())

            self.joystickTwo.LeftMiddleTop.whenPressed(ToggleLayoutCommand())

            self.joystickTwo.ClimbL3.whenPressed(L3ClimbCommandGroup())
            self.joystickTwo.ClimbL2.whenPressed(L2ClimbCommandGroup())
            self.joystickTwo.RightMiddleBottom.whenPressed(HoldUpCommandGroup())

            self.joystickTwo.leftThumb.whenPressed(ExtendRightCommand())
            self.joystickTwo.rightThumb.whenPressed(ExtendLeftCommand())

            self.joystickTwo.RightRightTop.whenPressed(ResetCommand())

            # The controller for non-driving subsystems of the robot
            self.controllerOne = LogitechDualShock(2)

            self.controllerOne.Back.whenPressed(ResetCommand())
            self.controllerOne.B.whenPressed(DeelevateCommand())

            self.controllerOne.X.whileHeld(DeelevateCommand())
            self.controllerOne.Y.whileHeld(ElevateCommand())

            self.controllerOne.DPadUp.whenPressed(ElevatorGoToLevelCommand('cargoBalls'))
            self.controllerOne.DPadDown.whenPressed(ElevatorGoToLevelCommand('lowBalls'))

            self.controllerOne.RightJoystick.toggleWhenPressed(IntakeCommand())

        else:

            # The controller for driving the robot

            self.controllerOne = LogitechDualShock(0)

            logicalaxes.driveX = self.controllerOne.RightX
            logicalaxes.driveY = self.controllerOne.RightX
            logicalaxes.driveRotate = self.controllerOne.LeftY

            self.controllerOne.LeftTrigger.whileHeld(GoToTapeCommand())
            self.controllerOne.LeftBumper.whileHeld(GoPastTapeCommand())

            self.controllerOne.B.whenPressed(EjectCommand())

            self.controllerOne.Start.whenPressed(L3ClimbCommandGroup())
            self.controllerOne.Back.whenPressed(L2ClimbCommandGroup())

            self.controllerOne.DPadUp.whenPressed(HoldUpCommandGroup())
            self.controllerOne.DPadDown.whileHeld(RearRetractCommand())

            self.controllerOne.LeftJoystick.whenPressed(ToggleSpeedCommand())
            self.controllerOne.DPadLeft.whileHeld(AllRetractCommand())

            self.controllerOne.DPadRight.whileHeld(FrontRetractCommand())

            self.controllerOne.X.whileHeld(ForceLowerCommand())

            self.controllerOne.RightBumper.whileHeld(ElevateCommand())

            self.controllerOne.Y.whenPressed(DeelevateCommand())
            self.controllerOne.RightTrigger.whileHeld(DeelevateCommand())

            self.controllerOne.A.toggleWhenPressed(IntakeCommand())

            # The self.controllerTwo for non-driving subsystems of the robot (Operator)
            self.controllerTwo = LogitechDualShock(1)

            self.controllerTwo.Back.whenPressed(ResetCommand())
            self.controllerTwo.B.whenPressed(DeelevateCommand()) # Pressing it sends it down all the way. (B on 2019 Scoring bot.)

            self.controllerTwo.Y.whenPressed(DeelevateCommand())
            self.controllerTwo.RightTrigger.whileHeld(DeelevateCommand())
            self.controllerTwo.RightBumper.whileHeld(ElevateCommand())

            self.controllerTwo.X.whileHeld(ForceLowerCommand())

            self.controllerTwo.DPadUp.whenPressed(ElevatorGoToLevelCommand('cargoBalls'))
            self.controllerTwo.DPadDown.whenPressed(ElevatorGoToLevelCommand('lowBalls'))

            #self.controllerOne.DPadRight.whileHeld(FrontRetractCommand())

            self.controllerTwo.A.toggleWhenPressed(IntakeCommand())
