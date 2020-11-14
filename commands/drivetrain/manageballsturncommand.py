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
        self.drivetrainWidth = 35 # Not really, still trying to figure crap out.

    def initialize(self):
        '''Calculates new positions by offseting the current ones.'''

        robot.intake.intakeBalls()
        
        robot.revolver.setCustomRR(0.5)
        if robot.revolver.isEmpty():
            robot.revolver.stopRevolver()
        else:
            robot.revolver.setVariableSpeed(-0.2)

        offset = math.copysign(self._calculateDisplacement(), self.degrees)

        print('offset ' + str(offset))

        self.targetPositions = []

        for position in robot.drivetrain.getPositions():
            self.targetPositions.append(position + offset)

        robot.drivetrain.setPositions(self.targetPositions, falconOverride=True, neoOverride=True)
        
    def execute(self):
        if robot.revolver.isEmpty():
            robot.revolver.stopRevolver()
        else:
            robot.revolver.setVariableSpeed(-0.2)
        print('pos ' + str(robot.drivetrain.getPositions()))
        print('tar ' + str(self.targetPositions))

    def end(self):
        robot.drivetrain.stop()
        robot.drivetrain.setProfile(0)
        
        robot.intake.stopIntake()
        robot.pneumatics.retractIntakeSolenoid()
        
        robot.revolver.stopRevolver()
        robot.revolver.enableRampRate()

    def _calculateDisplacement(self):
        '''
        In order to avoid having a separate ticksPerDegree, we calculate it
        based on the width of the robot base.
        '''

        inchesPerDegree = (math.pi * self.drivetrainWidth) / 360 #Config('DriveTrain/width') / 360 # 24.5 degrees to radians
        totalDistanceInInches = self.distance * inchesPerDegree
        units = robot.drivetrain.inchesToUnits(totalDistanceInInches)

        return units

        #return units #* Config('DriveTrain/slip', 1.2)
