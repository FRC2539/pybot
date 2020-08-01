from wpilib.command import InstantCommand

import robot


class TuneDownHoodCommand(InstantCommand):

    def __init__(self):
        super().__init__('Tune Down Hood')

    def initialize(self):
        robot.hood.downLLHood()
