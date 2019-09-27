from wpilib.command.commandgroup import CommandGroup
from .solidredcommand import SolidRedCommand
from .solidorangecommand import SolidOrangeCommand
from .solidgreencommand import SolidGreenCommand
from .solidbluecommand import SolidBlueCommand
import commandbased.flowcontrol as fc

class TwelveDaysOfChristmasLightsCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Twelve Days Of Christmas Lights')

        # Add commands here with self.addSequential() and self.addParallel()
        self.addSequential(SolidRedCommand())
