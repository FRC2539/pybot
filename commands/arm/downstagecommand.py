from wpilib.command.command import Command

import robot

class DownStageCommand(Command):

    def __init__(self, target=-3.0):
        super().__init__('Down Stage')

        self.requires(robot.arm)
        self.target = target


    def initialize(self):
        self._isFinished = False

        self.startPos = robot.arm.getPosition()


    def execute(self):
        robot.arm.setPosition(self.startPos + self.target, 'down')
        self._isFinished = robot.arm.getPosition() <= self.startPos + self.target


    def isFinished(self):
        return self._isFinished


    def end(self):
        robot.arm.stop()
