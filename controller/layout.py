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

from commands.intake.intakecommand import IntakeCommand
from commands.intake.ejectcommand import EjectCommand
from commands.intake.slowejectcommand import SlowEjectCommand

from commands.elevator.elevatecommand import ElevateCommand
from commands.elevator.deelevatecommand import DeelevateCommand
from commands.elevator.elevatorgotolevelcommand import ElevatorGoToLevelCommand

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

        selectedLayout = Config('/DriveTrain/Layout', 0)

        if selectedLayout == 0:
            self.joystickOne = LogitechJoystick(0)
            self.joystickTwo = LogitechJoystick(1)

            logicalaxes.driveX = self.joystickOne.X
            logicalaxes.driveY = self.joystickOne.Y

            logicalaxes.driveRotate = self.joystickTwo.X

            self.joystickOne.trigger.whileHeld(GoToTapeCommandGroup())
            self.joystickOne.bottomThumb.whileHeld(GoPastTapeCommand())

            self.joystickOne.Button6.whileHeld(RearRetractCommand())
            self.joystickOne.Button7.whenPressed(lrSecondAutoCommandGroup())

            self.joystickOne.Button8.whenPressed(lrAutoCommandGroup())
            self.joystickOne.Button9.whenPressed(rrAutoCommandGroup())

            self.joystickOne.Button10.whenPressed(rrSecondAutoCommandGroup())

            self.joystickTwo.trigger.whenPressed(EjectCommand())

            self.joystickTwo.Button6.whenPressed(ToggleLayoutCommand())

            self.joystickTwo.Button8.whenPressed(L3ClimbCommandGroup())
            self.joystickTwo.Button9.whenPressed(L2ClimbCommandGroup())

            self.joystickTwo.Button11.whenPressed(ResetCommand())

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

            logicalaxes.driveX = self.controllerOne.LeftX
            logicalaxes.driveY = self.controllerOne.LeftY
            logicalaxes.driveRotate = self.controllerOne.RightX

            self.controllerOne.LeftTrigger.whileHeld(GoToTapeCommand())
            self.controllerOne.LeftBumper.whileHeld(GoPastTapeCommand())

            self.controllerOne.A.whenPressed(ToggleFieldOrientationCommand())
            self.controllerOne.RightTrigger.whenPressed(EjectCommand())

            self.controllerOne.Start.whenPressed(L3ClimbCommandGroup())
            self.controllerOne.Back.whenPressed(L2ClimbCommandGroup())

            self.controllerOne.RightJoystick.whenPressed(ToggleLayoutCommand())


            # The self.controllerTwo for non-driving subsystems of the robot
            self.controllerTwo = LogitechDualShock(1)

            self.controllerTwo.Back.whenPressed(ResetCommand())
            self.controllerTwo.B.whenPressed(DeelevateCommand()) # Pressing it sends it down all the way. (B on 2019 Scoring bot.)

            self.controllerTwo.X.whileHeld(DeelevateCommand())
            self.controllerTwo.Y.whileHeld(ElevateCommand())

            self.controllerTwo.DPadUp.whenPressed(ElevatorGoToLevelCommand('cargoBalls'))
            self.controllerTwo.DPadDown.whenPressed(ElevatorGoToLevelCommand('lowBalls'))

            self.controllerTwo.RightJoystick.toggleWhenPressed(IntakeCommand())
