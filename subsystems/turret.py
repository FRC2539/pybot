from .debuggablesubsystem import DebuggableSubsystem

import ports
from ctre import ControlMode, FeedbackDevice, WPI_TalonSRX

class Turret(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Turret')
        self.motor = WPI_TalonSRX(ports.turret.motorID)
        self.motor.config_kP(0, .0001, 0)
        self.motor.config_kI(0, 0, 0)
        self.motor.config_kD(0, .001, 0)
        self.motor.config_kF(0, .00019, 0)
        self.motor.config_kIntegralZone(0, 0, 0)

    def move(self, speed):
        self.motor.set(ControlMode.PercentOutput, speed)

    def stop(self):
        self.motor.stopMotor()

    def setPosition(self, position):
        self.motor.set(ControlMode.Position, position)
