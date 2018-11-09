from .debuggablesubsystem import DebuggableSubsystem
from custom import driverhud

from wpilib import Spark
import ports


class Lights(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Lights')
        self.lights = Spark(ports.lights.lightControllerID)
        self.lights.setSafetyEnabled(False)
        self.lights.setInverted(False)
        self.variedcolor = -0.99

    def set(self, pulseWidth):
        self.lights.set(pulseWidth)

    def off(self):
        self.set(0.99)

    def solidOrange(self):
        self.set(0.65)

    def solidRed(self):
        self.set(0.61)

    def solidGreen(self):
        self.set(0.77)

    def solidBlue(self):
        self.set(0.87)

    def decreaseCycle(self):
        if self.variedcolor == -0.99:
            self.variedcolor = 0.99
            self.set(self.variedcolor)
            driverhud.showAlert('Speed Decrased:\n' + self.variedcolor)
        else:
            self.variedcolor -= 0.02
            self.set(self.variedcolor)
            driverhud.showAlert('Speed Decreased:\n' + self.variedcolor)

    def increaseCycle(self):
        if self.variedcolor == 0.99:
            self.variedcolor = -0.99
            self.set(self.variedcolor)
            driverhud.showAlert('Speed Increased:\n' + self.variedcolor)
        else:
            self.variedcolor += 0.02
            self.set(self.variedcolor)
            driverhud.showAlert('Speed Increased:\n' + self.variedcolor)
