from wpilib.command import Command

import robot


class TuneUpHoodCommand(Command):

    def __init__(self):
        super().__init__('Tune Up Hood')



    def initialize(self):
        robot.hood.upLLHood()


    def execute(self):
        pass


    def end(self):
        pass
