from wpilib.command import CommandGroup
from custom.config import Config

from commands.shooter.firecommand import FireCommand
from commands.shooter.gotoboilercommand import GoToBoilerCommand
from commands.shooter.turntoboilercommand import TurnToBoilerCommand


class ShootCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('ShootCommandGroup')

        self.addSequential(TurnToBoilerCommand())
        self.addSequential(GoToBoilerCommand())
        self.addSequential(FireCommand(Config('Shooter/speed')))
