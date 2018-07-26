from wpilib.command import CommandGroup
import commandbased.flowcontrol as fc
from custom.config import Config

from commands.drivetrain.pivotcommand import PivotCommand
from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.turncommand import TurnCommand
from commands.intake.intakecommand import IntakeCommand
class AutonomousCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Autonomous')

        self.addSequential(MoveCommand(48))
        self.addSequential(TurnCommand(90))
        self.addParallel(IntakeCommand(1))
        self.addSequential(MoveCommand(50))
