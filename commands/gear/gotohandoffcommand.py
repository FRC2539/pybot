from commands.drive.movecommand import MoveCommand

import subsystems
from custom.config import Config


class GoToHandoffCommand(MoveCommand):
    '''
    Drives the robot forward until it reaches the handoff distance, using
    encoders.
    '''

    def __init__(self):
        super().__init__(0, 'Drive to Handoff')


    def initialize(self):
        distance = subsystems.gear.getLiftDistance()
        distance -= Config('Gear/HandOffDistance')

        self.distance = distance

        super().initialize()
