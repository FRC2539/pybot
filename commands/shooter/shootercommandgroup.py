from wpilib.command.commandgroup import CommandGroup
import commandbased.flowcontrol as fc
from commands.shooter.shootcommand import ShootCommand
from commands.indexwheel.indexforwardcommand import IndexForwardCommand
from wpilib.command.waitcommand import WaitCommand

class ShooterCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Shooter')
        # Add commands here with self.addSequential() and self.addParallel()
        self.addParallel(ShootCommand(), 2)
        self.addSequential(WaitCommand(2))
        self.addSequential(IndexForwardCommand(), 3)
