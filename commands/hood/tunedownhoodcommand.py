from wpilib.command import Command

import robot


class TuneDownHoodCommand(Command):

    def __init__(self):
        super().__init__('Tune Down Hood')



    def initialize(self):
        robot.hood.downLLHood()


    def execute(self):
        pass


    def end(self):
        pass
