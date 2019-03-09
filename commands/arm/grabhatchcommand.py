from wpilib.command.command import Command

import robot

class GrabHatchCommand(Command):

    def __init__(self):
        super().__init__('Grab Hatch')

        self.requires(robot.arm)


    def initialize(self):
        self._isFinished = False
        self.originalPos = robot.arm.getPosition()
        robot.arm.setPosition(float(robot.arm.getPosition() + 10.0), 'up')


    def execute(self):
        if robot.arm.getPosition() > self.originalPos + 10.0:
            self._isFinished = True


    def isFinished(self):
        return self._isFinished


    def end(self):
        robot.arm.stop()
