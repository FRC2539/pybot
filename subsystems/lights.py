from .debuggablesubsystem import DebuggableSubsystem
from wpilib.relay import Relay

import ports

class Lights(DebuggableSubsystem):
    '''
    A system designed for turning the lights on and off.
    '''
    def __init__(self):
        super().__init__('Lights')

        self.lights = []
        for portID in ports.lights:
            self.lights.append(
                Relay(ports.lights[portID], Relay.Direction.kReverse)
            )

    def initDefaultCommand(self):
        '''
        By default, unless another command is running that requires this
        subsystem, twinkle the lights
        '''
        from commands.lights.standbycommand import StandbyCommand

        self.setDefaultCommand(StandbyCommand())


    def on(self, ID):
        self.lights[ID].set(Relay.Value.kOn)


    def off(self, ID):
        self.lights[ID].set(Relay.Value.kOff)
