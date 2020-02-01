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

        return self.distance

    def execute(self):
        pass
