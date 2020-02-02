from .debuggablesubsystem import DebuggableSubsystem

import ports

import math
from custom.config import Config
from networktables import NetworkTables


class Limelight(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Limelight')
        self.tv = Config('limelight/tv', 0)
        self.tx = Config('limelight/tx', 0)
        self.ty = Config('limelight/ty', 0)
        self.ta = Config('limelight/ta', 0)

        self.LimelightHeight = 19.55
        self.TargetHeight = 106.75
        self.calDistance = 120

        self.nt = NetworkTables.getTable('limelight')

        self.calAngle = math.atan((self.TargetHeight-self.LimelightHeight)/self.calDistance)
        print(str(self.calAngle))

    def setPipeline(self, pipeline: int):
        self.nt.putNumber('pipeline', pipeline)

    def getX(self):
        return self.tx.getValue()

    def getY(self):
        return self.ty.getValue()

    def getA(self):
        return self.ta.getValue()

    def getTape(self):
        return self.tv.getValue()

    def calcDistance(self):
        self.height = self.TargetHeight - self.LimelightHeight
        self.angle = self.calAngle  + math.radians(Limelight.getY())
        self.distance = self.height/math.tan(self.angle)
        return self.distance
