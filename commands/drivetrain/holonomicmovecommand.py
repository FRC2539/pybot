from wpilib.command.command import Command
import math
import robot
from custom.config import Config

class HolonomicMoveCommand(Command):

    def __init__(self, x, y, rotate):
        super().__init__('Holonomic Move')

        self.requires(robot.drivetrain)

        self.x = x
        self.y = y
        self.rotate = rotate

        self.targets = []


    def initialize(self):
        if robot.drivetrain.isFieldOriented:
            robot.drivetrain.toggleFieldOrientation()
        robot.drivetrain.resetGyro()
        positions = robot.drivetrain.getPositions()

        inchesPerDegree = (math.pi * 23.5) / 360
        totalDistanceInInches = self.rotate * inchesPerDegree
        ticks = (totalDistanceInInches / (math.pi * 6)) * 4096

        self.x = int(robot.drivetrain.strafeInchesToTicks(self.x))
        self.y = int(self.y / (math.pi * 6) * 4096)
        self.rotate = int(ticks * 1.2)

        self.targets = [
            positions[0] + self.x + self.y + self.rotate,
            positions[1] - self.x + self.y - self.rotate,
            positions[2] - self.x + self.y + self.rotate,
            positions[3] + self.x + self.y - self.rotate
        ]

        print("current")
        print(positions)
        print("targets")
        print(self.targets)

        robot.drivetrain.setPositions(self.targets)
