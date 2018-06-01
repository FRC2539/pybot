from wpilib.command import CommandGroup
from custom.config import Config

from commands.shooter.firecommand import FireCommand


class ShootCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('ShootCommandGroup')

        self.addSequential(TurnToBoilerCommand())
        self.addSequential(GoToBoilerCommand())
        self.addSequential(FireCommand(Config('Shooter/speed', 250)))
