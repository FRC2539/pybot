from .debuggablesubsystem import DebuggableSubsystem

import ports

import math
from custom.config import Config
from networktables import NetworkTables


class Limelight(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Limelight')
        self.nt = NetworkTables.getTable('limelight')
        self.tv = Config('limelight/tv', 0)
        self.tx = Config('limelight/tx', 1)
        self.ty = Config('limelight/ty', 0)
        self.ta = Config('limelight/ta', 0)

        self.LimelightHeight = 20
        self.TargetHeight = 106.75
        self.calDistance = 120

        self.calAngle = math.atan((self.TargetHeight-self.LimelightHeight)/self.calDistance)
        print(str(self.calAngle))

    def setPipeline(self, pipeline: int):
        self.nt.putNumber('pipeline', pipeline)

    def getX(self):
        return self.nt.getEntry('tx').getDouble(0)


    def getY(self):
        return self.nt.getEntry('ty').getDouble(0)

    def getA(self):
        return self.nt.getEntry('ta').getDouble(0)

    def getTape(self):
        return self.nt.getEntry('tv').getDouble(0)

    def calcDistance(self):
        self.height = self.TargetHeight - self.LimelightHeight
        #self.angle = self.calAngle  + math.radians(Limelight.getY(self))
        self.angle = math.radians(36.098 + self.getY())
        self.distance = self.height/math.tan(self.angle)
        return self.distance
