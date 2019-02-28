from wpilib.command.command import Command

import robot

class ForceRaiseCommand(Command):

    def __init__(self):
        super().__init__('Force Raise')

        self.requires(robot.arm)


    def initialize(self):
        self._isFinished = robot.arm.forceUp()


    def execute(self):
        self._isFinished = robot.arm.forceUp()


    def isFinished(self):
        if self._isFinished:
            return 1

    def end(self):
        robot.arm.stop()
