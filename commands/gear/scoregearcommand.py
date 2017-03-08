from wpilib.command.conditionalcommand import ConditionalCommand

from .scoregearcommandgroup import ScoreGearCommandGroup
from ..alertcommand import AlertCommand
from commands.drive.movecommand import MoveCommand
import subsystems

class ScoreGearCommand(ConditionalCommand):

    def __init__(self, distance=0):
        #self.alert = AlertCommand('Unknown error')
        super().__init__(
            self,
            ScoreGearCommandGroup(),
            MoveCommand(distance)
        )


    def condition(self):
        if not subsystems.gear.hasGear():
            #self.alert.setMessage('No gear loaded')
            print('no gear loaded')
            return False

        if not subsystems.gear.isLiftVisible():
            #self.alert.setMessage('Lift not visible')
            print('Lift not visible')
            return False

        return True
