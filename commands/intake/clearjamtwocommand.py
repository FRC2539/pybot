from threading import Timer # Well. This is fun.

from wpilib.command import Command
from wpilib import Timer

import robot

class ClearJamTwoCommand(Command):

    def __init__(self):
        super().__init__('Clear Jam Two')

        self.requires(robot.intake)

        self.timer = Timer(2.5, robot.intake.changeFumble())

    def initialize(self):
        robot.intake.fumbleForward()
        self.timer.start() # Switch directions every two seconds

    def end(self):
        robot.intake.stop()
        self.timer.cancel()
