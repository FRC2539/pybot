
from wpilib.command import CommandGroup

from custom.config import Config

from ..drive.movecommand import MoveCommand
from ..drive.turncommand import TurnCommand
from commands.shooter.checkforshootercommand import CheckForShooterCommand
from commands.shooter.firecommand import FireCommand

class StartWithShooterLeftCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('StartWithShooterCommandGroup')

        """self.addSequential(MoveCommand(95))
        self.addSequential(MoveCommand(-85))
        self.addSequential(TurnCommand(90))
        self.addSequential(MoveCommand(15))
        self.addSequential(FireCommand(Config('Shooter/speed')))"""

        self.addSequential(FireCommand(Config('Shooter/speed')), 9)
        self.addSequential(MoveCommand(20))
        self.addSequential(TurnCommand(-50))
        self.addSequential(MoveCommand(100))
