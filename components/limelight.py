import wpilib
import math
from custom.config import Config
from networktables import NetworkTables

class Limelight:

    def setup(self):
        self.tv = Config('limelight/tv', 0)
        self.tx = Config('limelight/tx', 0)
        self.ty = Config('limelight/ty', 0)
        self.ta = Config('limelight/ta', 0)

        self.nt = NetworkTables.getTable('limelight')

    def setPipline(self, pipeline: int):
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
        Limelight.setPipline(1)
        self.ht = 106.75
        self.hl = 20
        self.height = self.ht - self.hl
        #for the initial value that the y is added to, do arctan of self.height/(calibration distance)
        #calibraiton distacne should be 10 feet or 120 because this is in inches
        self.angle = 35.6519 + Limelight.getY()
        self.angle = math.radians(self.angle)
        self.distance = (self.height)/(math.tan(self.angle))
        Limelight().setPipline(0)

        return self.distance

    def execute(self):
        pass
