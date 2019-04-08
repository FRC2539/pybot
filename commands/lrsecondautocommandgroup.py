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

from commands.drivetrain.gototapecommand import GoToTapeCommand
from commands.drivetrain.gopasttapecommand import GoPastTapeCommand

from commands.intake.intakecommand import IntakeCommand
from commands.intake.ejectcommand import EjectCommand
from commands.intake.slowejectcommand import SlowEjectCommand


class lrSecondAutoCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('lr Auto')
        self.addSequential(SetPipelineCommand(0))

        #self.addParallel(SetArmCommandGroup(12.0))

        #mid hatch
        self.addParallel(SetArmCommandGroup(10.0, 80.0))

        self.addSequential(TransitionMoveCommand(35,95,25,90,30,-35))
        #self.addSequential(SuperStructureGoToLevelCommand("floor"))

        self.addSequential(StrafeCommand(-72))
        self.addSequential(GoToTapeCommand(), 3)
        self.addSequential(MoveCommand(2), 1)


        #self.addSequential(WaitCommand(.5))
        self.addParallel(SetArmCommandGroup(0.0, 0.0))
        self.addSequential(MoveCommand(-3), 1)
        self.addSequential(HolonomicMoveCommand(0,-160,305))
        #self.addSequential(MoveCommand(-18))
        #self.addSequential(TransitionMoveCommand(-50,80,-85,150,1,190))
        #self.addSequential(TurnCommand(182))
        #self.addSequential(TransitionMoveCommand(80,80,25,96))

        self.addSequential(GoToTapeCommand())
        #self.addParallel(SetArmCommandGroup(20.0))
        self.addSequential(MoveCommand(1))
        self.addSequential(RaiseCommand(), .75)
        self.addParallel(SetArmCommandGroup(11.0))
        #self.addSequential(TransitionMoveCommand(-100,-100,-85,-170,1,-55))

        self.addSequential(HolonomicMoveCommand(40,136,20))
        #self.addSequential(StrafeCommand(-50))
        self.addSequential(HolonomicMoveCommand(-55,0,25))
        self.addSequential(GoToTapeCommand())
        self.addSequential(MoveCommand(2))
        self.addSequential(LowerCommand())
        self.addSequential(MoveCommand(-5))
        # Add commands here with self.addSequential() and self.addParallel()
