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
        # Return the x value to correct for the limelight being rotated.
        return self.nt.getEntry('tx').getDouble(0)

    def getX(self):
        # Return the y value to correct for the limelight being rotated.
        return self.nt.getEntry('ty').getDouble(0)

    def getA(self):
        return self.nt.getEntry('ta').getDouble(0)

    def getTape(self):
        # Return whether or not tape is being detected by the limelight.
        if (self.nt.getEntry('tv').getDouble(0) == 1):
            return True
        return False

    def takeSnapShot(self):
        # Have the limelight take a snapshot.
        # These can be viewed by connecting to the limelight.
        self.nt.putNumber('snapshot', 1)

    def onTarget(self):
        # The limelight is on target if it can see tape
        # and the tape is centered in limelight's field of view.
        if self.getTape():
            if self.getX() < .75:
                return True
            else:
                return False
        else:
            return False

    def updateNetworkTables(self):
        pass
