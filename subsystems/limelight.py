from .cougarsystem import *

import ports
import robot
import math

from custom.config import Config
from networktables import NetworkTables

class Limelight(CougarSystem):
    '''Subsystem for interacting with the limelight.'''

    def __init__(self):
        super().__init__('Limelight')

        self.nt = NetworkTables.getTable('limelight')
        self.tv = Config('limelight/tv', 0)
        self.tx = Config('limelight/tx', 0)
        self.ty = Config('limelight/ty', 0)
        self.ta = Config('limelight/ta', 0)

        self.driveTable = NetworkTables.getTable('DriveTrain')
        
        # Set the range of velocities. 
        self.maxShooterRPM = 5600
        self.minShooterRPM = 3800

        self.setPipeline(1)

        self.closeShot = True

    def setPipeline(self, pipeline: int):
        self.nt.putNumber('pipeline', pipeline)

    def getY(self):
        return self.nt.getEntry('tx').getDouble(0)

    def getX(self):
        return self.nt.getEntry('ty').getDouble(0)

    def getA(self):
        return self.nt.getEntry('ta').getDouble(0)

    def getTape(self):
        if (self.nt.getEntry('tv').getDouble(0) == 1):
            return True
        return False

    def takeSnapShot(self):
        self.nt.putNumber('snapshot', 1)

    def generateVelocity(self, area, limit, longShot=False): 
        # Return the calculated velocity based off of the distance, in inches.
        return min(self.minShooterRPM + (limit - abs(area) / 0.0007), self.maxShooterRPM)

    def areaDistance(self):
        self.aDistance = math.log(self.getA(), .992924) + 221.996
        return self.aDistance

    def onTarget(self):
        if self.getTape():
            if self.getX() < .75:
                return True
            else:
                return False
        else:
            return False

    def getCamTran(self):
        return self.nt.getEntry('camTran').getDoubleArray([])

    def updateNetworkTables(self):
        self.driveTable.putNumberArray('camTran', self.getCamTran())
        self.driveTable.putNumber('distance', self.calcDistance())
    
    # TODO reconsider adding this if there is a turret and other methods use it.
    # def getFeildAngle(self):
    #     self.goal = robot.turret.getFieldPosition()
    #     self.aimed = robot.turret.getPosition()
    #     self.theta = ((self.goal - self.aimed)*360)/4096 + self.getX()
    #     return self.theta
