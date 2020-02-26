#from threading import Timer # Well. This is fun.

from wpilib.command import Command

from wpilib import Timer

import robot

class ClearJamTwoCommand(Command):

    def __init__(self):
        super().__init__('Clear Jam Two')

        self.requires(robot.intake)
        self.timer = Timer()

    def initialize(self):
        self.timer.start()
        robot.intake.fumbleForward()
        robot.intake.intakeFreakOutNT()

    def execute(self):
        if robot.intake.forward:
            if self.timer.get() % 1.5 < 0.01:
                robot.intake.changeFumble()
        else:
            if self.timer.get() % 1 < 0.01:
                robot.intake.changeFumble()

    def end(self):
        robot.intake.stop()
        self.timer.stop()
        self.timer.reset()
