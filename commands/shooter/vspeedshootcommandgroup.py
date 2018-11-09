from wpilib.command.commandgroup import CommandGroup
import commandbased.flowcontrol as fc
from commands.shooter.variedspeedshootcommand import VariedSpeedShootCommand
from commands.indexwheel.indexforwardcommand import IndexForwardCommand
from wpilib.command.waitcommand import WaitCommand

class VariedSpeedShootCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Slow Shooter')
        # Add commands here with self.addSequential() and self.addParallel()
        self.addParallel(VariedSpeedShootCommand(), 2)
        self.addSequential(WaitCommand(2))
        self.addSequential(IndexForwardCommand(), 2)
