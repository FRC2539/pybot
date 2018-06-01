
from wpilib.command import CommandGroup

from custom.config import Config

from ..drive.movecommand import MoveCommand
from ..drive.turncommand import TurnCommand
from commands.shooter.checkforshootercommand import CheckForShooterCommand
from commands.shooter.firecommand import FireCommand

class StartWithShooterRightCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('StartWithShooterCommandGroup')



        self.addSequential(FireCommand(Config('Shooter/speed', 250)), 9)
        self.addSequential(MoveCommand(20))
        self.addSequential(TurnCommand(10))
        self.addSequential(MoveCommand(10))
        self.addSequential(TurnCommand(70))
        self.addSequential(MoveCommand(100))
