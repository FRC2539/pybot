from wpilib.command.command import Command

import robot

class DownResetCommand(Command):

    def __init__(self):
        super().__init__('Down Reset')

        self.requires(robot.elevator)


    def initialize(self):
        self._finished = robot.elevator.downReset()


    def execute(self):
        self._finished = robot.elevator.downReset()


    def isFinished(self):
        return self._finished


    def end(self):
        robot.elevator.stop()
