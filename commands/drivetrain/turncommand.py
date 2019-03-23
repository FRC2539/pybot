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


    def initialize(self):
        '''Calculates new positions by offseting the current ones.'''
        robot.drivetrain.setSpeedLimit(2500)

        offset = self._calculateDisplacement()
        targetPositions = []
        for position in robot.drivetrain.getPositions():
            targetPositions.append(position + offset)

        robot.drivetrain.setPositions(targetPositions)


    def _calculateDisplacement(self):
        '''
        In order to avoid having a separate ticksPerDegree, we calculate it
        based on the width of the robot base.
        '''
        print('Turn width ' + str(Config('DriveTrain/width').getValue()))

        inchesPerDegree = math.pi / 180 #* float(Config('DriveTrain/width').getValue()) / 360.0
        totalDistanceInInches = self.distance * inchesPerDegree
        ticks = robot.drivetrain.inchesToTicks(totalDistanceInInches)

        return ticks * Config('DriveTrain/slip', 1.2)
