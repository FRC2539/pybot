from .debuggablesubsystem import DebuggableSubsystem
from ctre import WPI_TalonSRX, ControlMode, NeutralMode

import ports


class Dropper(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Dropper')
        self.motor = WPI_TalonSRX(ports.dropper.motorID)
        self.motor.setNeutralMode(NeutralMode.Brake)
        self.motor.setSafetyEnabled(False)


    def slowDrop(self):
        self.motor.set(-0.6)


    def shoot(self):
        self.motor.set(-1)


    def returnObject(self):
        self.motor.set(0.3)


    def stop(self):
        self.motor.set(0)
