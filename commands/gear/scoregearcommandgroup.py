from wpilib.command.commandgroup import CommandGroup
from commandbased.cancelcommand import CancelCommand

from .aligngearcommand import AlignGearCommand
from .drivetoliftcommand import DriveToLiftCommand
from ..drive.setspeedcommand import SetSpeedCommand
from custom.config import Config
import custom.flowcontrol as fc
import subsystems


class ScoreGearCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Score Gear')

        self.addSequential(SetSpeedCommand(400))
        self.addSequential(AlignGearCommand(Config('Gear/HandOffDistance', 100)))
        @fc.IF(subsystems.gear.isLiftVisible)
        def hangTheGear(self):
            self.addSequential(DriveToLiftCommand(), 4)
