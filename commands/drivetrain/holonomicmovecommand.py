from wpilib.command.timedcommand import TimedCommand
import math
import robot
from custom.config import Config

class HolonomicMoveCommand(TimedCommand):

    def __init__(self, x, y, rotate):

        #Fix this lol it's really dumb
        self.originalX = x
        self.originalY = y
        self.originalRotate = rotate

        self.xTime = 0
        self.yTime = 0
        self.rotateTime = 0

        self.xTicks = 0
        self.yTicks = 0
        self.rotateTicks = 0

        self.runtimeSecs = 0
        self.runtime = 0
        self.speedLimit = robot.drivetrain.speedLimit #2800

        self.setup()

        super().__init__('Holonomic Move', self.calcTimeout())

        self.requires(robot.drivetrain)


    def setup(self):
        print("holo setup")
        self.x = self.originalX
        self.y = self.originalY
        self.rotate = self.originalRotate


    def calcTimeout(self):
        inchesPerDegree = (math.pi * 23.5) / 360
        totalDistanceInInches = self.rotate * inchesPerDegree
        ticks = (totalDistanceInInches / (math.pi * 6)) * 4096

        self.xTicks = robot.drivetrain.strafeInchesToTicks(self.x)
        self.yTicks = (self.y / (math.pi * 6) * 4096)
        self.rotateTicks = (ticks * 1.5)

        self.xTime = self.xTicks / (self.speedLimit * 10)
        self.yTime = self.yTicks / (self.speedLimit * 10)
        self.rotateTime = self.rotateTicks / (self.speedLimit * 10)

        self.runtimeSecs = 2 * (math.sqrt((self.xTime ** 2) + (self.yTime ** 2) + (self.rotateTime ** 2)))
        print("calcTimeout: "+ str(self.runtimeSecs))
        return self.runtimeSecs


    def initialize(self):
        print("holo init")
        self.setup()

        if not robot.drivetrain.isFieldOriented:
            robot.drivetrain.toggleFieldOrientation()
        #robot.drivetrain.resetGyro()
        print("holo init runtime: "+str(self.runtime))
        self.runtime = self.runtimeSecs * 10 * 1.15

        self.x = (self.xTicks / self.runtime) / (self.speedLimit / 2)
        self.y = (self.yTicks / self.runtime) / (self.speedLimit / 2)
        self.rotate = ((self.rotateTicks * 1.2) / self.runtime) / (self.speedLimit / 2)

        print('X:          ' + str(self.x))
        print('Y:          ' + str(self.y))
        print('Rotate:     ' + str(self.rotate))


    def execute(self):
        robot.drivetrain.move(self.x, self.y, self.rotate)

        print('X:          ' + str(self.x))
        print('Y:          ' + str(self.y))
        print('Rotate:     ' + str(self.rotate))


    def end(self):
        robot.drivetrain.stop()
        #if robot.drivetrain.getAngle() != self.originalRotate and [self.originalX, self.originalY] != [0, 0]:
            #adjust(self.originalRotate - robot.drivetrain.getAngle())


def adjust(adjustment):
    HolonomicMoveCommand(0, 0, adjustment).start()
