from wpilib.command.command import Command

import robot

class ElevateCommand(Command):

    def __init__(self):
        super().__init__('Elevate')

        self.requires(robot.elevator)


    def initialize(self):
        self._finished = False


    def execute(self):
        self._finished = robot.elevator.up()
        print(robot.elevator.getPosition())


    def isFinished(self):
        return self._finished


    def end(self):
        robot.elevator.stop()
