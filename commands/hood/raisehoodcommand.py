from wpilib.command import Command

import robot

class RaiseHoodCommand(Command):

    def __init__(self):
        super().__init__('Raise Hood')

        self.requires(robot.hood)

    def initialize(self):
        robot.hood.raiseHood()

    def isFinished(self):
        print('h ' + str(robot.hood.getPosition()))
        return robot.hood.atHighest()

    def end(self):
        robot.hood.stopHood()
        #print('\n\n\n\nDONE\n\n\n\n')
