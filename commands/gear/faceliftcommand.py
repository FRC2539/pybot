from wpilib.command.command import Command
from commands.drive.turncommand import TurnCommand
import subsystems
from custom.config import Config

class FaceLiftCommand(TurnCommand):
    '''
    Calculates the needed turn based on the vision target offset, then performs
    a single turn to make the needed correction.
    '''

    def __init__(self):
        super(TurnCommand, self).__init__(0, 'Face Lift')


    def initialize(self):
        distance = subsystems.gear.getLiftCenter()

        if abs(distance) <= 10:
            distance = 0

        distance /= Config('Gear/pixelsPerDegree', 10)
        self.distance = distance

        super().initialize()
