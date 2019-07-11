from wpilib.command.command import Command

import robot

class MaintainPositionCommand(Command):

    def __init__(self):
        super().__init__('Maintain Position')

        self.requires(robot.climber)


    def initialize(self):
        self._finished = False
        self.startPos = robot.climber.getAvgPosition()


    def execute(self):
        if robot.climber.getAvgPosition() < self.startPos:
            robot.climber.popAll()

        if robot.climber.getAvgPosition() >= self.startPos:
            robot.climber.stopRacks()

        robot.climber.creepBackward()

    def end(self):
        robot.climber.stopDrive()
