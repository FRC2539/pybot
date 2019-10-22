from .debuggablesubsystem import DebuggableSubsystem

from wpilib import Relay as WPIRelay

import ports


class Relay(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Relay')
        self.relay = WPIRelay(ports.relay.relayDIO)

    def setForward(self):
        self.relay.set(WPIRelay.Value.kOn)
    def stop(self):
        self.relay.set(WPIRelay.Value.kOff)
    def changeDirection(self, direction):
        if direction:
            self.relay.setDirection(WPIRelay.Direction.kForwardOnly)
        else:
            return self.relay.setDirection(WPIRelay.Direction.kReverseOnly)
    def getState(self):
        return self.relay.get()
