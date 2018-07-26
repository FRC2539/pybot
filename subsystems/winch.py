from .debuggablesubsystem import DebuggableSubsystem

import ports
from ctre import WPI_TalonSRX


class Winch(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Winch')

        self.winch = WPI_TalonSRX(ports.winch.mainmotor)
        self.winch.setSafetyEnabled(False)

    def moveWinch(self, speed=1):
        self.winch.set(speed)
