from wpilib.command import CommandGroup
import commandbased.flowcontrol as fc
from custom.config import Config

from commands.network.alertcommand import AlertCommand

from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.turncommand import TurnCommand

class AutonomousCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Autonomous')
        self.addSequential(MoveCommand(96))
