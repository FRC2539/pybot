from .debuggablesubsystem import DebuggableSubsystem
from ctre import WPI_TalonSRX, ControlMode, NeutralMode

import ports


class Intake(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Intake')
        self.motor = WPI_TalonSRX(ports.intake.motorID)
        self.motor.setNeutralMode(NeutralMode.Brake)
        self.motor.setSafetyEnabled(False)


    def intake(self):
        self.motor.set(0.8)


    def reverse(self):
        self.motor.set(-0.4)


    def slowIntake(self):
        self.motor.set(0.6)


    def stop(self):
        self.motor.set(0)
