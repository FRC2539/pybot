from wpilib.command import Command

import robot

class LowerHoodCommand(Command):

    def __init__(self):
        super().__init__('Lower Hood')

        self.requires(robot.hood)

    def initialize(self):
        robot.hood.lowerHood()

    def isFinished(self):
        #print(robot.hood.getPosition())
        return robot.hood.atLowest()

    def end(self):
        robot.hood.stopHood()
        #print('\n\n\n\nDONE\n\n\n\n')
