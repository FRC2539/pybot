from wpilib.command import CommandGroup
from wpilib.command import PrintCommand
from wpilib.driverstation import DriverStation
from custom.config import Config
from commands.network.alertcommand import AlertCommand
from wpilib.command.waitcommand import WaitCommand
import commandbased.flowcontrol as fc

from networktables import NetworkTables

import robot

from commands.drivetrain.strafecommand import StrafeCommand
from commands.drivetrain.movewithgyrocommand import MoveWithGyroCommand
from commands.drivetrain.zerogyrocommand import ZeroGyroCommand
from commands.drivetrain.visionmovecommand import VisionMoveCommand
from commands.drivetrain.transitionmovecommand import TransitionMoveCommand
from commands.drivetrain.turntocommand import TurnToCommand
from commands.drivetrain.turncommand import TurnCommand
from commands.drivetrain.strafecommand import StrafeCommand
from commands.drivetrain.pivotcommand import PivotCommand
from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.setspeedcommand import SetSpeedCommand
from commands.drivetrain.togglefieldorientationcommand import ToggleFieldOrientationCommand
from commands.drivetrain.holonomicmovecommand import HolonomicMoveCommand
from commands.drivetrain.setpipelinecommand import SetPipelineCommand

from commands.arm.setarmcommandgroup import SetArmCommandGroup
from commands.arm.lowercommand import LowerCommand
from commands.arm.raisecommand import RaiseCommand

from commands.drivetrain.gototapecommandgroup import GoToTapeCommandGroup
from commands.drivetrain.gopasttapecommand import GoPastTapeCommand

from commands.intake.intakecommand import IntakeCommand
from commands.intake.ejectcommand import EjectCommand
from commands.intake.slowejectcommand import SlowEjectCommand


class lrAutoCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('lr Auto')
        #self.addParallel(HatchIntakeCommand())
        self.addParallel(LowerCommand())

        self.addSequential(TransitionMoveCommand(80,80,35,50,0,0))
        self.addSequential(HolonomicMoveCommand(-100,20,-65))
        #tf
        #self.addSequential(TransitionMoveCommand(80,80,35,45,0,0))
        #self.addSequential(HolonomicMoveCommand(85,11,65))

        self.addSequential(GoToTapeCommandGroup(), 5)

        self.addSequential(HolonomicMoveCommand(20,-90,235))#305305
        #tf
        #self.addSequential(HolonomicMoveCommand(20,-105,-250))#305
        self.addSequential(GoToTapeCommandGroup(), 5)

        self.addSequential(HolonomicMoveCommand(40,100,35))
        self.addSequential(HolonomicMoveCommand(-63,0,0))
        self.addSequential(GoToTapeCommandGroup(), 5)
        self.addSequential(HolonomicMoveCommand(24,-60,-45))
