from wpilib.command.conditionalcommand import ConditionalCommand

from .scoregearcommandgroup import ScoreGearCommandGroup
from ..alertcommand import AlertCommand
import subsystems

class ScoreGearCommand(ConditionalCommand):

    def __init__(self):
        super().__init__(
            'Score Gear',
            ScoreGearCommandGroup(),
            AlertCommand('Lift is not visible')
        )


    def condition(self):
        return subsystems.gear.isLiftVisible()
