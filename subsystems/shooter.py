from wpilib.command import Subsystem

from .cougarsystem import *

from rev import CANSparkMax, IdleMode, MotorType, ControlType

import ports

class Shooter(Subsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Shooter')

        self.motorOne = CANSparkMax(ports.shooter.motorOneID, MotorType.kBrushless)
        self.encoderOne = self.motorOne.getEncoder()
        self.controllerOne = self.motorOne.getPIDController()

        self.motorTwo = CANSparkMax(ports.shooter.motorTwoID, MotorType.kBrushless)
        self.encoderTwo = self.motorTwo.getEncoder()
        self.controllerTwo = self.motorTwo.getPIDController()

        self.motorTwo.follow(self.motorOne, True) # True to invert the motor

    def setRPM(self, rpm):
        self.controllerOne.setReference(rpm, ControlType.Velocity, 0, 0)

    def reverseShooter(self):
        self.motorOne.set(-0.4)

    def stopShooter(self):
        self.motorOne.stopMotor()

    def getRPM(self): # Returns the average RPM
        return (self.encoderOne.getVelocity() + self.encoderTwo.getVelocity()) / 2

