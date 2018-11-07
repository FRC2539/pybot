from .debuggablesubsystem import DebuggableSubsystem

from wpilib import Spark
import ports


class Lights(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Lights')
        self.lights = Spark(ports.lights.lightControllerID)
        self.lights.setSafetyEnabled(False)
        self.lights.setInverted(False)

    def set(self, pulseWidth):
        self.lights.set(pulseWidth)

    def off(self):
        self.set(0.99)

    def solidOrange(self):
        self.set(0.09)

    def solidRed(self):
        self.set(0.61)

    def solidGreen(self):
        self.set(0.77)

    def solidBlue(self):
        self.set(0.87)
