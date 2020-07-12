from .debuggablesubsystem import DebuggableSubsystem

from rev import ControlType, MotorType, IdleMode, CANSparkMax

from wpilib import DigitalInput

import ports

import math

class Revolver(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Revolver')

        self.motor = CANSparkMax(ports.revolver.motorID, MotorType.kBrushless)

        self.motor.setIdleMode(IdleMode.kBrake)
        self.motor.setInverted(False) # CC is negative, C is positive

        self.encoder = self.motor.getEncoder()

        self.controller = self.motor.getPIDController()

        self.controller.setP(0.001, 0)
        self.controller.setI(0.0, 0)
        self.controller.setD(0.0, 0)
        self.controller.setIZone(0.0, 0)
        self.controller.setFF(0.0, 0)

        self.gearRatio = 1.5

    def spinCounterClockwise(self):
        self.motor.set(-0.2)

    def spinClockwise(self):
        self.motor.set(0.2)

    def resetEncoder(self):
        self.encoder.setPosition(0.0)

    def getPosition(self): # returns ROTATIONS
        return self.encoder.getPosition() / self.gearRatio

    def getAngle(self): # returns DEGREES
        return ((self.getPosition() % 1) * 360)

    def goToZero(self):
        self.encoder.setReference(round(self.getPosition()), ControlType.kPosition, 0, 0)

    def setAngle(self, angle):
        angle %= 360 # Ensure that it's all positive, 0-360.

        diff = (angle - self.getAngle())

        if abs(diff) > 180: # #turnthecararound!
            diff = math.copysign((360 - max([self.getAngle(), angle])) + min([self.getAngle(), angle]), self.getAngle() - angle) # RIP 99.999% of my brain cells.

        diff /= 360

        self.controller.setReference((diff + self.getPosition()) * self.gearRatio, ControlType.kPosition, 0, 0)
