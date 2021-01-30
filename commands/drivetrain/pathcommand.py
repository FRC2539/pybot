from wpilib.command import Command
import math

import robot


class PathCommand(Command):
    def __init__(self):
        super().__init__("Path")

        self.requires(robot.drivetrain)

    def initialize(self):
        self.lastPositions = robot.drivetrain.getPositions()
        self.lastSlope = [0, 0, 0, 0]
        self.totalDisplacements = [0, 0, 0, 0]
        self.speeds = [0.25, 0.25, 0.25, 0.25]
        # test path = x squared
        # test dy/dx = 2x

    def execute(self):

        currentPositions = robot.drivetrain.getPositions()
        displacements = []

        for lPosition, cPosition in zip(self.lastPositions, currentPositions):
            displacements.append(cPosition - lPosition)

        for i, (d, m) in enumerate(zip(displacements, self.lastSlope)):
            if m == 0:
                self.totalDisplacements[i] += d
            else:
                self.totalDisplacements[i] += d * 1 / m

        self.lastSlope = []
        angle = []

        for dx in self.totalDisplacements:
            angle.append(math.atan(2(dx)))
            self.lastSlope.append(2(dx))

        avg = sum(angle) / len(angle)
        robot.drivetrain.setModuleAngles(avg)
        robot.drivetrain.setSpeeds(self.speeds)

        """
        displacements will be the distance along the x axis that has been traveled
        always starting at 0,0
        """

    def end(self):
        pass
