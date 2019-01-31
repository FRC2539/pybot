from wpilib.command.timedcommand import TimedCommand
import math
import robot
from custom.config import Config

class HolonomicMoveCommand(TimedCommand):

    def __init__(self, x, y, rotate):

        self.x = x
        self.y = y
        self.rotate = rotate

        self.xTime = 0
        self.yTime = 0
        self.rotateTime = 0

        self.runtime = 0
        self.speedLimit = robot.drivetrain.speedLimit

        super().__init__('Holonomic Move', self.calcTimeout())

        self.requires(robot.drivetrain)



    def calcTimeout(self):
        inchesPerDegree = (math.pi * 23.5) / 360
        totalDistanceInInches = self.rotate * inchesPerDegree
        ticks = (totalDistanceInInches / (math.pi * 6)) * 4096

        self.x = robot.drivetrain.strafeInchesToTicks(self.x)
        self.y = (self.y / (math.pi * 6) * 4096)
        self.rotate = (ticks * 1.2)

        self.xTime = self.x / (self.speedLimit * 10)
        self.yTime = self.y / (self.speedLimit * 10)
        self.rotateTime = self.rotate / (self.speedLimit * 10)

        self.runtime = self.yTime
        if self.xTime > self.runtime:
            self.runtime = self.xTime
        if self.rotateTime > self.runtime:
            self.runtime = self.rotateTime

        print(self.runtime)
        return self.runtime


    def initialize(self):
        if robot.drivetrain.isFieldOriented:
            robot.drivetrain.toggleFieldOrientation()
        robot.drivetrain.resetGyro()

        self.runtime = self.runtime * 10

        self.x = (self.x / self.runtime) / self.speedLimit
        self.y = (self.y / self.runtime) / self.speedLimit
        self.rotate = ((self.rotate * 1.2) / self.runtime) / self.speedLimit

        print('X:          ' + str(self.x))
        print('Y:          ' + str(self.y))
        print('Rotate:     ' + str(self.rotate))


    def execute(self):
        robot.drivetrain.move(self.x, self.y, self.rotate)


    def isFinished(self):
        if self.isTimedOut():
            robot.drivetrain.stop()
            return True
        else:
            return False


    def end(self):
        robot.drivetrain.stop()
