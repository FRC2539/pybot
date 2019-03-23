from wpilib.command.command import Command

import robot

class BumpUpCommand(Command):

    def __init__(self, target):
        super().__init__('Bump Up')

        self.requires(robot.elevator)
        self.target = target


    def initialize(self):
        self._isFinished = False

        if robot.elevator.getPosition() >= robot.elevator.upperLimit:
            self._isFinished = True


    def execute(self):
        print("elevator bumpup pos: "+str(robot.elevator.getPosition()))
        self._isFinished = robot.elevator.setPosition(self.target, 'up')


    def isFinished(self):
        return self._isFinished


    def end(self):
        robot.elevator.stop()
