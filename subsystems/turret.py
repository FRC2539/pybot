from .debuggablesubsystem import DebuggableSubsystem

from ctre import WPI_VictorSPX

import ports


class Turret(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Turret')
        self.motor = WPI_VictorSPX(ports.turret.motorID)
        self.motor.setSafetyEnabled(False)

    def raiseTurret(self):
        self.motor.set(0.25)

    def lowerTurret(self):
        self.motor.set(-0.18)

    def slowRaise(self):
        self.motor.set(0.25)

    def slowLower(self):
        self.motor.set(-0.18)

    def stop(self):
        self.motor.set(0)
