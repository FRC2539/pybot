from wpilib.command import CommandGroup

from custom.config import Config

from ..drive.movecommand import MoveCommand
from ..drive.turncommand import TurnCommand
from ..drive.gotoliftcommand import GoToLiftCommand

class HangGearCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('HangGearCommandGroup')

        self.addSequential(MoveCommand(48))
        self.addSequential(TurnCommand(Config("Autonomous/robotLocation")))
        self.addSequential(GoToLiftCommand())





