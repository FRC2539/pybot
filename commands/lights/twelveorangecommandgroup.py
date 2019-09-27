from wpilib.command.commandgroup import CommandGroup
from .solidorangecommand import SolidOrangeCommand
import commandbased.flowcontrol as fc

class twelveorangeCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('twelveorange')

        # Add commands here with self.addSequential() and self.addParallel()
        self.addSequential(SolidOrangeCommand())
