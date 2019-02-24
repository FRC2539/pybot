from wpilib.command.command import Command

import robot

class ForceLowerCommand(Command):

    def __init__(self):
        super().__init__('Force Lower')

        self.requires(robot.arm)


    def initialize(self):
        self._isFinished = robot.arm.forceDown()


    def execute(self):
        self._isFinished = robot.arm.forceDown()


    def isFinished(self):
        if self._isFinished:
            return 1


    def end(self):
        robot.arm.stop()
