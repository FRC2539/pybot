from wpilib.command.commandgroup import CommandGroup
from commandbased.stopcommand import StopCommand

from .aligngearcommand import AlignGearCommand
from ..drive.setspeedcommand import SetSpeedCommand
from ..drive.gotowallcommand import GoToWallCommand
from ..pickup.pickupcommand import PickupCommand
from custom.config import Config


class ScoreGearCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Score Gear')

        self.addParallel(PickupCommand())
        self.addSequential(SetSpeedCommand(500))
        self.addSequential(AlignGearCommand(Config('Gear/HandOffDistance', 36)))
        self.addSequential(GoToWallCommand())
        self.addSequential(StopCommand(self))
