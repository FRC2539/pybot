from wpilib.command import Command

import robot

class RunDownUntilImpactCommand(Command):

    def __init__(self):
        super().__init__('Run Down Until Impact')

        self.requires(robot.colorwheel)

    def initialize(self):
        robot.colorwheel.reverseSpin()

    def isFinished(self):
        return robot.colorwheel.stopOnImpact()

    def end(self):
        robot.colorwheel.stopRaise()
