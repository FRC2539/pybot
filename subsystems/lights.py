from .debuggablesubsystem import DebuggableSubsystem
from custom import driverhud
from wpilib import Spark
from networktables import NetworkTables

import ports

class Lights(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Lights')
        self.lights = Spark(ports.lights.lightControllerID)


    '''
    Light Mapping:
        Intake:     - Has Game Piece:       Solid Green

        Auto:       - No Target             Solid Red
                    - Sees Target, Moving   Blink Purple (fast)
                    - In position           Solid Blue

        Loading:    - Hatch Panel           Blink Yellow (fast)
                    - Cargo                 Blink Pink (fast)

        Seizure Mode at end of match        Seizure Mode

        Issue                               Blink Red (slow)
    '''


    def set(self, pulseWidth):
        self.lights.set(pulseWidth)

    def setSpecific(self, val):
        self.set(val)

    def off(self):
        self.set(0.99)

    def solidRed(self):
        self.set(0.61)

    def solidGreen(self):
        self.set(0.71)

    def solidYellow(self):
        self.set(0.69)

    def solidBlue(self):
        self.set(0.83)

    def solidWhite(self):
        self.set(0.93)

    def solidPink(self):
        self.set(0.57)

    def solidOrange(self):
        self.set(0.63)

    def solidViolet(self):
        self.set(0.91)

    def fire(self):
        self.set(-0.57)

    def chase(self):
        self.set(-0.31)
