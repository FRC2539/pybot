from .debuggablesubsystem import DebuggableSubsystem
from ctre import WPI_TalonSRX, ControlMode, NeutralMode

import ports


class Shooter(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Shooter')
        self.motor = WPI_TalonSRX(ports.shooter.motorID)
        self.motor.setNeutralMode(NeutralMode.Brake)
        self.motor.setSafetyEnabled(False)

# Do not touch anything above this

    def fastShoot(self):
        self.motor.set(1)


    def mediumShoot(self):
        self.motor.set(0.7)


    def slowShoot(self):
        self.motor.set(0.5)


    def stop(self):
        self.motor.set(0)
