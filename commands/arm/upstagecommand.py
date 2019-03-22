from wpilib.command.command import Command

import robot

class UpStageCommand(Command):

    def __init__(self, target):
        super().__init__('Up Stage')

        self.requires(robot.arm)
        self.target = target


    def initialize(self):
        self._isFinished = False

        if robot.arm.getPosition() >= robot.arm.upperLimit:
            self._isFinished = True


    def execute(self):
        print("arm upstage pos: "+str(robot.arm.getPosition()))
        self._isFinished = robot.arm.setPosition(self.target, 'up')


    def isFinished(self):
        return self._isFinished


    def end(self):
        robot.arm.stop()
