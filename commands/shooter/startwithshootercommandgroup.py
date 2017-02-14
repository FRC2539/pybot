
from wpilib.command import CommandGroup

from custom.config import Config

from ..drive.movecommand import MoveCommand
from ..drive.turncommand import TurnCommand
from commands.shooter.gotoboilercommand import GoToBoilerCommand
from commands.shooter.turntoboilercommand import TurnToBoilerCommand
from commands.shooter.checkforshootercommand import CheckForShooterCommand

class StartWithShooterCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('StartWithShooterCommandGroup')

        #self.addSequential(MoveCommand(48))
        self.addSequential(TurnCommand(Config("Autonomous/robotLocation")))
        self.addSequential(CheckForShooterCommand())
