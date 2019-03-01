from wpilib.command.command import Command

import robot

class ExtendRearCommand(Command):

    def __init__(self):
        super().__init__('Extend Rear')

        self.requires(robot.climber)


    def initialize(self):
        self._finished = False


    def execute(self):
        self._finished = robot.climber.extendRear()


    def isFinished(self):
        return self._finished


    def end(self):
        robot.climber.stopRacks()
