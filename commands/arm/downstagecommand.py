from wpilib.command.command import Command
from custom.config import Config

import robot

class DownStageCommand(Command):

    def __init__(self):
        super().__init__('Down Stage')

        self.requires(robot.arm)

        self.targetNT = Config('Arm/slackAdjustment', -3.0)
        self.speedNT = Config('Arm/slackSpeed', -8)


    def initialize(self):
        self._isFinished = False

        self.startPos = robot.arm.getPosition()
        self.target = float(self.targetNT.getValue())
        self.speed = float(self.speedNT.getValue() / 100)


    def execute(self):
        robot.arm.set(self.speed)
        self._isFinished = robot.arm.getPosition() <= self.startPos + self.target


    def isFinished(self):
        return self._isFinished


    def end(self):
        robot.arm.stop()
