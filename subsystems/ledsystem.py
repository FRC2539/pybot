from .cougarsystem import *

from wpilib.command import Subsystem

from wpilib import Spark

import ports

class LEDSystem(CougarSystem):
    '''Manages a part of the LED system on the robot.'''

    def __init__(self):
        super().__init__('LEDSystem')

        self.LEDController = Spark(ports.ledsystem.controllerID)

        disablePrints()

    def set(self, f):
        self.LEDController.set(f)

    def off(self):
        self.set(0.99)

    def setGreen(self):
        self.set(0.77)

    def setRed(self):
        self.set(0.61)

    def setBlue(self):
        self.set(0.87)

    def setOrange(self):
        self.set(0.65)

    def setYellow(self):
        self.set(0.65)

    def setWhite(self):
        self.set(0.93)

    def rainbowLava(self):
        self.set(-0.93)

    def colorOneChase(self):
        self.set(0.01)

    def whiteHeartbeat(self):
        self.set(-0.21)

    def blueHeartbeat(self):
        self.set(-0.23)
        
    def redHeartbeat(self):
        self.set(-0.17)

    def colorOneHeartbeat(self): # ORANGE
        self.set(0.25)
    
    def colorOneStrobe(self):
        self.set(0.15)
    
    def colorTwoHeartbeat(self): # GREEN
        self.set(0.05)
