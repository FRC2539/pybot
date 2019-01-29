from wpilib.command.timedcommand import TimedCommand
import math
import robot
from custom.config import Config

class HolonomicMoveCommand(TimedCommand):

    def __init__(self, x, y, rotate, timeout):
        super().__init__('Holonomic Move', timeout)

        self.requires(robot.drivetrain)

        self.x = x
        self.y = y
        self.rotate = rotate

        self.cycles = timeout * 10
        self.speedLimit = robot.drivetrain.speedLimit


    def initialize(self):
        if robot.drivetrain.isFieldOriented:
            robot.drivetrain.toggleFieldOrientation()
        robot.drivetrain.resetGyro()

        inchesPerDegree = (math.pi * 23.5) / 360
        totalDistanceInInches = self.rotate * inchesPerDegree
        ticks = (totalDistanceInInches / (math.pi * 6)) * 4096

        self.x = ((robot.drivetrain.strafeInchesToTicks(self.x) / self.cycles) / self.speedLimit)
        self.y = 3 * (((self.y / (math.pi * 6) * 4096) / self.cycles) / self.speedLimit)
        self.rotate = 2 * (((ticks * 1.2) / self.cycles) / self.speedLimit)

        print('X:          ' + str(self.x))
        print('Y:          ' + str(self.y))
        print('Rotate:     ' + str(self.rotate))

        robot.drivetrain.move(self.x, self.y, self.rotate)

    def execute(self):
        pass

    def isFinished(self):
        if self.isTimedOut():
            robot.drivetrain.stop()
            return True
        else:
            return False

    def end(self):
        robot.drivetrain.stop()
