from wpilib.command import CommandGroup

from custom.config import Config

from ..drive.movecommand import MoveCommand
from ..drive.turncommand import TurnCommand
from .waitforliftcommand import WaitForLiftCommand
from .scoregearcommand import ScoreGearCommand

# Initiate procedure for hanging the gear at the beginning of the match.
class GearAutonomousCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Score a Gear Autonomously')

        self.addSequential(MoveCommand(50))
        self.addSequential(TurnCommand(Config("Autonomous/robotLocation")))
        self.addSequential(WaitForLiftCommand())
        self.addSequential(ScoreGearCommand())
