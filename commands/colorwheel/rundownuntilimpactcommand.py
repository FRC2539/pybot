from wpilib.command import Command

from wpilib import Timer

import robot

class RunDownUntilImpactCommand(Command):

    def __init__(self):
        super().__init__('Run Down Until Impact')

        self.requires(robot.colorwheel)

        self.wwTimer = Timer()

    def initialize(self):
        robot.colorwheel.reverseSpin()
        self.wwTimer.start()

    def isFinished(self):
        return (self.wwTimer.get() >= 0.3)

    def end(self):
        robot.colorwheel.stopRaise()
        self.wwTimer.stop()
        self.wwTimer.reset()
