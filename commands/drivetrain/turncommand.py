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

        robot.drivetrain.resetGyro()

        self.degrees = degrees
        self.drivetrainWidth = 27.75

    def initialize(self):
        '''Calculates new positions by offseting the current ones.'''

        robot.drivetrain.setProfile(2)
        robot.drivetrain.resetGyro()
        
        self.goal = (robot.drivetrain.getAngle() + self.degrees) % 360

        offset = math.copysign(self._calculateDisplacement(), self.degrees)

        self.targetPositions = []

        for position in robot.drivetrain.getPositions():
            self.targetPositions.append(position + offset)

        robot.drivetrain.setPositions(self.targetPositions)

    def isFinished(self):
        
        for x in range(1000):
        
            print('\n\n\n\n\n\n goal ' + str(self.goal))
            print('\n\n\n\n\n\n my ang ' + str(robot.drivetrain.getAngle()))
        
        if self.degrees < 0:
            return robot.drivetrain.getAngleTo(self.goal) < 0                       
        else:
            return robot.drivetrain.getAngleTo(self.goal) > 0

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
