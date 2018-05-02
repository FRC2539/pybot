from wpilib.command import Command

import robot

class GoToHeightCommand(Command):

    def __init__(self, level):
        super().__init__('Go To %s' % level, 1)
        self.level = level

        self.requires(robot.elevator)


    def initialize(self):
        robot.elevator.setLevel(self.level)
        self.target = robot.elevator.floors[robot.elevator.level]
        self.stopped = 0


    def isFinished(self):
        if not self.isTimedOut():
            return False

        if abs(self.target - robot.elevator.getHeight()) > 1000:
            return False

        if robot.elevator.getSpeed() < 0.01:
            self.stopped += 1
        else:
            self.stopped = 0

        return self.stopped >= 5
