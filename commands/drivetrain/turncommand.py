from wpilib.command import Command

import robot
from custom.config import Config

import math


class TurnCommand(Command):
    """Allows autonomous turning using the drive base encoders."""

    def __init__(self, degrees, tolerance=3, name=None):
        if name is None:
            name = "Turn %f degrees" % degrees

        self.degrees = degrees
        self.tolerance = tolerance
        # Radius (in) * 2 * pi
        self.robotCircumference = 16.84251 * math.pi * 2

    def initialize(self):
        """Calculates new positions by offseting the current ones."""

        self.modulesInPosition = False
        self.turnSet = False

        self.targetAngles = [45, 135, -45, -135]

        # self.startAngle = robot.drivetrain.getAngle()

        # Rotate the swerve modules to a position where they can rotate in a circle.
        robot.drivetrain.setModuleAngles(self.targetAngles)

        self.targetDistance = self._calculateDisplacement()

    #def execute(self):
        #if self.modulesInPosition and not self.turnSet:
            #robot.drivetrain.setPositions(self.targetDistance)
            #self.turnSet = True
        #else:
            ## Compare the degrees within a tolerance of 3 degrees.
            #allAnglesWithinTolerance = True

            #for angle, targetAngle in zip(
            #    robot.drivetrain.getModuleAngles(), self.targetAngles
            #):
            #    if abs(angle - targetAngle) >= self.tolerance:
            #        allAnglesWithinTolerance = False

            #if allAnglesWithinTolerance:
            #    self.modulesInPosition = True

    #def end(self):
        #robot.drivetrain.stop()

    #def _calculateDisplacement(self):
        """Returns the distance (in) for the given degrees.
        This feeds into the drivetrain's positioning method,
        where the distance is based on the robot's circumference."""

        ## Angle -> percentage of the robot's circumference
        #return (self.degrees / 360) * self.robotCircumference
