
from wpilib.command import CommandGroup

from custom.config import Config

from ..drive.movecommand import MoveCommand
from ..drive.turncommand import TurnCommand
from commands.gear.gotoliftcommand import GoToLiftCommand
from commands.gear.turntoliftcommand import TurnToLiftCommand
from commands.gear.scoregearcommand import ScoreGearCommand

# Initiate procedure for hanging the gear at the beginning of the match.
class StartWithGearCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('StartWithGearCommandGroup')

        self.addSequential(MoveCommand(96))
        self.addSequential(TurnCommand(Config("Autonomous/robotLocation")))
        self.addSequential(ScoreGearCommand())
