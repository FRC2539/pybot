from wpilib.command import Command

import robot

class RunUpUntilImpactCommand(Command):

    def __init__(self):
        super().__init__('Run Until Impact')

        self.requires(robot.colorwheel)

    def initialize(self):
        robot.colorwheel.startSpin()

    def isFinished(self):
        print(robot.colorwheel.stopOnImpact())
        print('amp ' + str(robot.colorwheel.getAmp()))
        return robot.colorwheel.stopOnImpact()

    def end(self):
        robot.colorwheel.stopRaise()
