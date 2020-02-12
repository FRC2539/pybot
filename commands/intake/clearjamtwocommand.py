from wpilib.command import Command
from wpilib import Timer

import robot

class ClearJamTwoCommand(Command):

    def __init__(self):
        super().__init__('Clear Jam Two')

        self.requires(robot.intake)
        self.timer = Timer()

    def initialize(self):
        robot.intake.fumbleForward()
        self.timer.start()

    def execute(self):
        if self.timer.get() % 3 <= 1: # here's an operator I don't normally use lol.
            robot.intake.changeFumble()

    def end(self):
        robot.intake.stop()
        self.timer.stop()
