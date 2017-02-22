from wpilib.command.conditionalcommand import ConditionalCommand

from .scoregearcommandgroup import ScoreGearCommandGroup
from ..alertcommand import AlertCommand
import subsystems

class ScoreGearCommand(ConditionalCommand):

    def __init__(self):
        self.alert = AlertCommand('Unknown error')
        super().__init__(
            'Score Gear',
            ScoreGearCommandGroup(),
            self.alert
        )


    def condition(self):
        if not subsystems.gear.hasGear():
            self.alert.setMessage('No gear loaded')
            print('no gear loaded')
            return False

        if not subsystems.gear.isLiftVisible():
            self.alert.setMessage('Lift not visible')
            print('Lift not visible')
            return False

        return True
