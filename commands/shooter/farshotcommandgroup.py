from wpilib.command import CommandGroup
import commandbased.flowcontrol as fc

from commands.hood.setlaunchanglecommand import SetLaunchAngleCommand
from commands.shooter.shootcommand import ShootCommand

class FarShotCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Far Shot')

        # Add commands here with self.addSequential() and self.addParallel()

        self.addParallel(ShootCommand(4600))
        self.addParallel(SetLaunchAngleCommand(23))
