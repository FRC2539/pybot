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
        self.fDegrees = abs(self.degrees)

    def initialize(self):
        '''Calculates new positions by offseting the current ones.'''

        self.start = robot.drivetrain.getRawAngle()

        robot.drivetrain.setProfile(2)
        offset = self._calculateDisplacement()
        self.targetPositions = []
        for position in robot.drivetrain.getPositions():
            self.targetPositions.append(position + offset)




        ##print('pos ' + str(self.targetPositions))
        #robot.drivetrain.setPositions(self.targetPositions)

    #def isFinished(self):
        #''' Get the current angle to the desired position, and stop it if it's nearby. '''
        ##print(robot.drivetrain.getAngle())
        #if abs(robot.drivetrain.getAngleTo(self.degrees)) < 3:
            #robot.drivetrain.stop()
            ##print('done')
            #return True

        #print('pos ' + str(self.targetPositions))
        #robot.drivetrain.setPositions(self.targetPositions, False)

    ##def isFinished(self):
        ##''' Get the current angle to the desired position, and stop it if it's nearby. '''
        ##print(robot.drivetrain.getAngle())
        ##if abs(robot.drivetrain.getAngleTo(self.degrees)) < 3:
            ##robot.drivetrain.stop()
            ##print('done')
            ##return True

        ##return False


    def isFinished(self):
        print(' b ' + str(abs(self.start - robot.drivetrain.getRawAngle()) >= self.fDegrees))
        return (abs(self.start - robot.drivetrain.getRawAngle()) >= self.fDegrees)

    def end(self):
        robot.drivetrain.stop()
        robot.drivetrain.setProfile(0)

    def _calculateDisplacement(self):
        '''
        In order to avoid having a separate ticksPerDegree, we calculate it
        based on the width of the robot base.
        '''

        inches = self.degrees * math.pi / 180 * 18 # 12 is half of the db width.

        #inchesPerDegree = math.pi * 24.5 / 180.0 #Config('DriveTrain/width') / 360 # 24.5 degrees to radians
        #totalDistanceInInches = self.distance * inchesPerDegree
        #units = robot.drivetrain.inchesToUnits(totalDistanceInInches)

        return robot.drivetrain.inchesToUnits(inches)

        #return units #* Config('DriveTrain/slip', 1.2)
