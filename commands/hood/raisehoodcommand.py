from wpilib.command import Command

import robot

class RaiseHoodCommand(Command):

    def __init__(self):
        super().__init__('Raise Hood')

        self.requires(robot.hood)

    def initialize(self):
        robot.hood.raiseHood()

    def isFinished(self):
        if robot.hood.atHighest():
            robot.hood.stopHood()
            return True
        else:
            return False

    def end(self):
        robot.hood.stopHood()
        print('\n\n\n\nDONE\n\n\n\n')
