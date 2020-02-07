from .debuggablesubsystem import DebuggableSubsystem

import ports

import wpilib

class PneumaticSystems(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('PneumaticSystems')
        self.compressor = wpilib.Compressor(ports.pneumaticSystem.compressorPort) # Not much to implement.

    def enableCompressor(self):
        self.compressor.setClosedLoopControl(True) # Runs the compressor, use in pits.

    def isFull(self):
        return not self.compressor.getPressureSwitchValve() # Returns true when full, false when low.

    def disableCompressor(self):
        self.compressor.setClosedLoopControl(False)