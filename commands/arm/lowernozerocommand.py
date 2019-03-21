from wpilib.command.command import Command

import robot

class LowerNoZeroCommand(Command):

    def __init__(self):
        super().__init__('Lower No Zero')

        self.requires(robot.arm)


    def initialize(self):
        self._finished = False


    def execute(self):
        self._finished = robot.arm.downNoZero()


    def isFinished(self):
        return self._finished


    def end(self):
        robot.arm.stop()
