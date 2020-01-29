from .debuggablesubsystem import DebuggableSubsystem

from wpilib import Relay as WPIRelay

import ports


class Relay(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Relay')
        self.relay = WPIRelay(ports.relay.relayDIO)
        self.relay.stopMotor()

    def setForward(self):
        self.relay.set(WPIRelay.Value.kOn)

    def stop(self):
        self.relay.set(WPIRelay.Value.kOff)

    def getState(self):
        return self.relay.get()
