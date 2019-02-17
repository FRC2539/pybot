from wpilib.command.command import Command

import robot

class RaiseCommand(Command):

    def __init__(self):
        super().__init__('Raise')

        self.requires(robot.arm)


    def initialize(self):
        self._finished = False


    def execute(self):
        print('Arm:     ' + str(robot.arm.getPosition()))
        self._finished = robot.arm.up()


    def isFinished(self):
        return self._finished


    def end(self):
        robot.arm.stop()
