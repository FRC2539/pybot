from .movecommand import MoveCommand

import robot
from custom.config import Config

import math


class TurnCommand(MoveCommand):
    '''Allows autonomous turning using the drive base encoders.'''

    def __init__(self, degrees, name=None):
        if name is None:
            name = 'Turn %f degrees' % degrees

        super().__init__(degrees, False, name)

        self.degrees = degrees
        self.drivetrainWidth = 27.75

    def initialize(self):
        '''Calculates new positions by offseting the current ones.'''

        robot.drivetrain.resetGyro()
        robot.drivetrain.setProfile(2)

        offset = math.copysign(self._calculateDisplacement(), self.degrees)

        self.targetPositions = []

        for position in robot.drivetrain.getPositions():
            self.targetPositions.append(position + offset)

        robot.drivetrain.setPositions(self.targetPositions)

    def isFinished(self):
        return abs(robot.drivetrain.getAngleTo(self.degrees)) <= 1

    def end(self):
        robot.drivetrain.stop()
        robot.drivetrain.setProfile(0)


    def _calculateDisplacement(self):
        '''
        In order to avoid having a separate ticksPerDegree, we calculate it
        based on the width of the robot base.
        '''

        inchesPerDegree = math.pi * self.drivetrainWidth / 360
        totalDistanceInInches = self.distance * inchesPerDegree
        ticks = robot.drivetrain.inchesToTicks(totalDistanceInInches)

        return ticks #* Config('DriveTrain/slip', 1.2)
