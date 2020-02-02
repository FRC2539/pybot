from .debuggablesubsystem import DebuggableSubsystem

import ports

from rev import CANSparkMax, ControlType, MotorType


class Shooter(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Shooter')

        self.motor = CANSparkMax(ports.shooter.motorID, MotorType.kBrushless)
        self.encoder = self.motor.getEncoder()
        self.controller = self.motor.getPIDController()

        self.controller.setFF(0.00019 , 0)
        self.controller.setP(0.0001 , 0)
        self.controller.setI(0 , 0)
        self.controller.setD(0.001 , 0)
        self.controller.setIZone(0 , 0)

    def run(self, percent):
        self.motor.set(percent)

    def stop(self):
        self.motor.stopMotor()

    def getRPM(self):
        return self.encoder.getVelocity()

    def setRPM(self, rpm):
        self.controller.setReference(float(rpm), ControlType.kVelocity, 0, 0)
