from wpilib.command import CommandGroup

from commands.shooter.firecommand import FireCommand
from commands.drive.gotoboilercommand import GoToBoilerCommand
from commands.drive.turntoboilercommand import TurnToBoilerCommand

class ShootCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('ShootCommandGroup')

        self.addSequential(TurnToBoilerCommand())
        self.addSequential(GoToBoilerCommand())
        self.addSequential(FireCommand())
