from .debuggablesubsystem import DebuggableSubsystem

import ports

from wpilib import AnalogPotentiometer

class PotentiometerInterface(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('PotentiometerInterface')
        self.potentiometer = AnalogPotentiometer(0)
        self.potentiometerSpark = AnalogPotentiometer(1)

    def getReadingTalon(self):
        return self.potentiometer.get()

    def getReadingSpark(self):
        return self.potentiometerSpark.get()
