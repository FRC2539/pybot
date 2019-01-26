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
        self.lights.setSafetyEnabled(False)
        self.lights.setInverted(False)
        self.variedcolor = -0.99
        NetworkTables.initialize(server='roborio-2539-frc.local')
        lightTable = NetworkTables.getTable('Lights')
        lightTable.putBoolean('lightsOn', False)
        lightTable.putBoolean('killLights', False)

    def set(self, pulseWidth):
        self.lights.set(pulseWidth)

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
        self.set(0.65)

    def solidViolet(self):
        self.set(0.91)
