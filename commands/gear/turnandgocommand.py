from wpilib.command.instantcommand import InstantCommand

from commands.drive.movecommand import MoveCommand
from commands.drive.turncommand import TurnCommand

from custom.config import Config
import subsystems


class TurnAndGoCommand(InstantCommand):
    '''
    Uses vision to calculate the needed turn angle and distance to get to lift
    handoff distance, and creates commands that do that.
    '''

    def __init__(self):
        super().__init__('Turn and Go to Lift')

        self.turncommand = TurnCommand(0)
        self.movecommand = MoveCommand(0)


    def initialize(self):
        distance = subsystems.gear.getLiftCenter()

        if abs(distance) <= 10:
            distance = 0

        distance /= Config('Gear/pixelsPerDegree', 10)
        self.turncommand.distance = distance

        distance = subsystems.gear.getLiftDistance()
        distance -= Config('Gear/HandOffDistance', 15)

        distance = max(distance, 0)

        self.movecommand.distance = distance


    def turn(self):
        return self.turncommand


    def go(self):
        return self.movecommand
