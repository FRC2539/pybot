from wpilib.command import CommandGroup
from wpilib.command.conditionalcommand import ConditionalCommand

from custom.config import Config

from ..drive.movecommand import MoveCommand
from ..drive.turncommand import TurnCommand
from .waitforliftcommand import WaitForLiftCommand
from .scoregearcommand import ScoreGearCommand
from wpilib.command.waitcommand import WaitCommand

# Initiate procedure for hanging the gear at the beginning of the match.
class GearAutonomousCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Score a Gear Autonomously')

        move = ConditionalCommand('Move Toward Lift', MoveCommand(80))
        distance = 80
        if Config("Autonomous/robotLocation") != 0:
            distance = 30
        move.condition = lambda: Config("Autonomous/robotLocation") != 0
        self.addSequential(move)
        self.addSequential(WaitCommand(.5))
        self.addSequential(TurnCommand(Config("Autonomous/robotLocation")))
        self.addSequential(WaitForLiftCommand())
        self.addSequential(ScoreGearCommand(distance))
