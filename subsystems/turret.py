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
        self.motor.config_IntegralZone(0, 0, 0)
        self.max = 110
        self.min = -110

    def move(self, speed):

        if(self.motor.getSelectSensorPosition(0)>self.max and self.motor.getSelectSensorPosition(0)<self.min):
            self.motor.set(ControlMode.PercentOutput, speed)
        else:
            print('hit turret limit')
            self.motor.stopMotor()

    def stop(self):
        self.motor.stopMotor()

    def returnZero(self):
        self.motor.set(ControlMode.Position, 0)

    def setPosition(self, position):
        if (position > self.min and position < self.max):
            self.motor.set(ControlMode.Position, position)
        else:
            print('param past turret max')
            self.motor.stopMotor()
