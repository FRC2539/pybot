from wpilib.command import CommandGroup

from commands.shooter.firecommand import FireCommand

class ShootCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('ShootCommandGroup')

        self.addSequential(FireCommand())
