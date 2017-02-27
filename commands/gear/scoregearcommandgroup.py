from wpilib.command.commandgroup import CommandGroup
from commandbased.stopcommand import StopCommand
from wpilib.command.waitcommand import WaitCommand

from .aligngearcommand import AlignGearCommand
from ..drive.setspeedcommand import SetSpeedCommand
from ..drive.gotowallcommand import GoToWallCommand
from ..pickup.pickupcommand import PickupCommand
from .waitonpilotcommand import WaitOnPilotCommand
from ..drive.movecommand import MoveCommand
from custom.config import Config


class ScoreGearCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Score Gear')

        pickup = PickupCommand()
        self.addParallel(PickupCommand())
        self.addSequential(SetSpeedCommand(500))
        self.addSequential(AlignGearCommand(Config('Gear/HandOffDistance')))
        #self.addSequential(GoToWallCommand())
        self.addSequential(StopCommand(pickup))
        self.addSequential(WaitOnPilotCommand())
        self.addSequential(WaitCommand(0.5))
        self.addSequential(MoveCommand(-24))
