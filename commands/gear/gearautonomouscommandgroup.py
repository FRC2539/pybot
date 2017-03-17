from wpilib.command import CommandGroup
from wpilib.command.conditionalcommand import ConditionalCommand
from wpilib.command.waitcommand import WaitCommand

from custom.config import Config
import subsystems

from ..drive.movecommand import MoveCommand
from ..drive.turncommand import TurnCommand
from .waitforliftcommand import WaitForLiftCommand
from .scoregearcommand import ScoreGearCommand
from .blindhangcommandgroup import BlindHangCommandGroup
from .waitonpilotcommand import WaitOnPilotCommand
from ..alertcommand import AlertCommand

# Initiate procedure for hanging the gear at the beginning of the match.
class GearAutonomousCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Score a Gear Autonomously')

        move = ConditionalCommand('Move Toward Lift', MoveCommand(80))
        move.condition = lambda: Config("Autonomous/robotLocation") != 0

        scoreAnyway = ConditionalCommand(
            'Attempt to Score',
            ScoreGearCommand(),
            BlindHangCommandGroup()
        )
        scoreAnyway.condition = lambda: subsystems.gear.isLiftVisible()

        self.addSequential(move)
        self.addSequential(WaitCommand(.5))
        self.addSequential(TurnCommand(Config("Autonomous/robotLocation")))
        self.addSequential(WaitForLiftCommand())
        self.addSequential(scoreAnyway)
        self.addSequential(WaitOnPilotCommand())
        self.addSequential(AlertCommand('Gear removed', 'Info'))
        self.addSequential(WaitCommand(0.5))
        self.addSequential(MoveCommand(-24))
