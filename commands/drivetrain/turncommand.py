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


    def initialize(self):
        '''Calculates new positions by offseting the current ones.'''
        robot.drivetrain.setProfile(2)
        offset = self._calculateDisplacement()
        self.targetPositions = []
        for position in robot.drivetrain.getPositions():
            self.targetPositions.append(position + offset)

        print('pos ' + str(self.targetPositions))
        robot.drivetrain.setPositions(self.targetPositions)

    def isFinished(self):
        ''' Get the current angle to the desired position, and stop it if it's nearby. '''
        print(robot.drivetrain.getAngle())
        if abs(robot.drivetrain.getAngleTo(self.degrees)) < 3:
            robot.drivetrain.stop()
            print('done')
            return True

        return False

    def end(self):
        robot.drivetrain.setProfile(0)
        robot.drivetrain.stop()

    def _calculateDisplacement(self):
        '''
        In order to avoid having a separate ticksPerDegree, we calculate it
        based on the width of the robot base.
        '''

        inchesPerDegree = math.pi * 25.75 / 360#Config('DriveTrain/width') / 360
        totalDistanceInInches = self.distance * inchesPerDegree
        units = robot.drivetrain.inchesToUnits(totalDistanceInInches)

        return units #* Config('DriveTrain/slip', 1.2)
