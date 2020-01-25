from .debuggablesubsystem import DebuggableSubsystem

from wpilib import Compressor
import ports


class Pneumatics(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Pneumatics')
        self.compressor = Compressor()

    def intake(self):
        self.compressor.start()

    def stopIntake(self):
        self.compressor.stop()

    def getStatus(self):
        return not self.compressor.getPressureSwitchValue()
        # Returns true if the pressure is full.

    def setLoopOn(self):
        self.compressor.setClosedLoopControl(True)

    def setLoopOff(self):
        self.compressor.setClosedLoopControl(False)
