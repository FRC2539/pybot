from .debuggablesubsystem import DebuggableSubsystem
from ctre import ControlMode, NeutralMode, WPI_TalonSRX

import ports


class Intake(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Intake')

        self.motor = WPI_TalonSRX(ports.intake.motorID)


    def intake(self):
        self.motor.set(0.5)


    def eject(self):
        self.motor.set(-1.0)


    def slowEject(self):
        self.motor.set(-0.6)


    def stop(self):
        self.motor.stopMotor()
