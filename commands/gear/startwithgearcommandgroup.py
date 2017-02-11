
from wpilib.command import CommandGroup

from custom.config import Config

from ..drive.movecommand import MoveCommand
from ..drive.turncommand import TurnCommand
from commands.gear.gotoliftcommand import GoToLiftCommand
from commands.gear.turntoliftcommand import TurnToLiftCommand
from commands.gear.checkforgearcommand import CheckForGearCommand

class StartWithGearCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('HangGearCommandGroup')

        self.addSequential(MoveCommand(48))
        self.addSequential(TurnCommand(Config("Autonomous/robotLocation")))
        self.addSequential(CheckForGearCommand())
