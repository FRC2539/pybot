#from .debuggablesubsystem import *

from wpilib.command import Subsystem

from .cougarsystem import *

import ports
import robot
import math
from custom.config import Config
from networktables import NetworkTables


class Limelight(CougarSystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Limelight')
        self.nt = NetworkTables.getTable('limelight')
        self.tv = Config('limelight/tv', 0)
        self.tx = Config('limelight/tx', 0)
        self.ty = Config('limelight/ty', 0)
        self.ta = Config('limelight/ta', 0)

        self.driveTable = NetworkTables.getTable('DriveTrain')

        self.LimelightHeight = 20
        self.TargetHeight = 98.25
        self.calDistance = 120

        self.llHeight = 19.5 # Height on robot.
        self.llAngle = 22 # Limelight angle in degrees, relative to the ground.

        self.setPipeline(1)

        #self.calAngle = math.atan((self.TargetHeight-self.LimelightHeight)/self.calDistance)
        #print(str(self.calAngle))

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

    def getCamTran(self):
        return self.nt.getEntry('camtran').getDoubleArray([])

    def get3D_X(self): # Left / Right
        return self.nt.getEntry('camtran').getDoubleArray([])[0]

    def get3D_Y(self):
        return self.nt.getEntry('camtran').getDoubleArray([])[1]

    def get3D_Z(self): # Distance?
        return self.nt.getEntry('camtran').getDoubleArray([])[2]

    def get3D_Pitch(self):
        return self.nt.getEntry('camtran').getDoubleArray([])[3]

    def get3D_Yaw(self):
        return self.nt.getEntry('camtran').getDoubleArray([])[4]

    def get3D_Roll(self):
        return self.nt.getEntry('camtran').getDoubleArray([])[5]

    def takeSnapShot(self):
        self.nt.putNumber('snapshot', 1)

    def generateVelocity(self, distance): # Returns the calculated velocity based off of the distance, in inches.
        if distance == 0.0:
            distance = self.calcDistanceGood()

        print('shooting with ' + str(distance))
        return min(4.6097902097902 * abs(distance) + 4264.6153846154, 5500)

    def calcDistance(self):
        self.height = self.TargetHeight - self.LimelightHeight
        #self.angle = self.calAngle  + math.radians(Limelight.getY(self))
        self.angle = math.radians(30.52289 + self.getY())
        self.distance = self.height/math.tan(self.angle)

        return self.distance

    def calcDistanceGood(self):
        self.height = 77.25
        self.angle = math.radians(30.52289 + self.getY())
        self.distance = self.height/math.tan(self.angle)
        #print(str(self.distance))
        return self.distance

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

    def getFeildAngle(self):
        self.goal = robot.turret.getFieldPosition()
        self.aimed = robot.turret.getPosition()
        self.theta = ((self.goal - self.aimed)*360)/4096 + self.getX()
        return self.theta

    def calcXDistance(self):
        self.theta = self.getFeildAngle()
        self.d = self.calcDistance()
        self.xD = math.sin(math.radians(self.theta)) * self.d
        return self.xD

    def calcYDistance(self):
        self.theta = self.getFeildAngle()
        self.d = self.calcDistance()
        self.yD = math.cos(math.radians(self.theta)) * self.d
        return self.yD

    def bensDistance(self):
        print('Y ' + str(self.getY()))
        return (98.25 - self.llHeight) / (math.tan(math.radians(self.llAngle + self.getY())))

    def updateNetworkTables(self):
        self.driveTable.putNumberArray('camTran', self.getCamTran())
        self.driveTable.putNumber('distance', self.calcDistance())
