from wpilib.command import InstantCommand

import robot


class TuneUpHoodCommand(InstantCommand):

    def __init__(self):
        super().__init__('Tune Up Hood')

    def initialize(self):
        robot.hood.upLLHood()

