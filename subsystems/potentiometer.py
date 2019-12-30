from .debuggablesubsystem import DebuggableSubsystem

import ports

from wpilib import AnalogPotentiometer

class PotentiometerInterface(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('PotentiometerInterface')
        self.potentiometer = AnalogPotentiometer(0)

    def getReading(self):
        return self.potentiometer.get()
