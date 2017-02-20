from wpilib.command import CommandGroup
from wpilib.command.waitcommand import WaitCommand

from custom.config import Config

from ..drive.movecommand import MoveCommand
from ..drive.turncommand import TurnCommand
from .scoregearcommand import ScoreGearCommand

# Initiate procedure for hanging the gear at the beginning of the match.
class StartWithGearCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('StartWithGearCommandGroup')

        self.addSequential(MoveCommand(96))
        self.addSequential(TurnCommand(Config("Autonomous/robotLocation")))
        self.addSequential(WaitCommand(0.5))
        self.addSequential(ScoreGearCommand())
