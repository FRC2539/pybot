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
        self.drivetrainWidth = 32.75

    def initialize(self):
        '''Calculates new positions by offseting the current ones.'''
        
        robot.drivetrain.stop()
        robot.drivetrain.setProfile(0)
        
        for x in range(1000):
            pass
        
        self.rawGoal = robot.drivetrain.navX.getAngle() + self.degrees

        #offset = math.copysign(self._calculateDisplacement(), self.degrees)

        #self.targetPositions = []

        #for position in robot.drivetrain.getPositions():
            #self.targetPositions.append(position + offset)

        #robot.drivetrain.setPositions(self.targetPositions)

    def execute(self):
        offset = self.rawGoal - robot.drivetrain.navX.getAngle()

        power = abs((offset) / (self.degrees * 1.5))

        power = math.copysign(min(max(power, 0.1), 0.6), self.degrees)

        print(power)
        
        robot.drivetrain.move(0, 0, power)

    def isFinished(self):
        if self.degrees < 0:
            return robot.drivetrain.navX.getAngle() <= self.rawGoal
        else:
            return robot.drivetrain.navX.getAngle() >= self.rawGoal

    def end(self):
        robot.drivetrain.stop()
        
        robot.drivetrain.resetEncoders()
        
        for x in range(100000):
            pass
            
    def _calculateDisplacement(self):
        '''
        In order to avoid having a separate ticksPerDegree, we calculate it
        based on the width of the robot base.
        '''

        inchesPerDegree = math.pi * self.drivetrainWidth / 360
        totalDistanceInInches = self.distance * inchesPerDegree
        ticks = robot.drivetrain.inchesToUnits(totalDistanceInInches)

        return ticks #* Config('DriveTrain/slip', 1.2)
