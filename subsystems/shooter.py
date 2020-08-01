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

        self.controllerOne.setFF(0.000171, 0)
        self.controllerOne.setP(0.0004, 0)
        self.controllerOne.setI(0, 0)
        self.controllerOne.setD(0.001, 0)
        self.controllerOne.setIZone(0, 0)

        self.motorTwo.follow(self.motorOne, True) # True to invert the motor

        self.shooting = False

        self.maxVel = 5800 # Experimental velocities.
        self.minVel = 2800

    def setRPM(self, rpm):
        self.shooting = True
        self.controllerOne.setReference(rpm, ControlType.kVelocity, 0, 0)

    def reverseShooter(self):
        self.shooting = True
        self.motorOne.set(-0.4)

    def stopShooter(self):
        self.motorOne.stopMotor()
        self.shooting = False

    def isShooting(self):
        return self.shooting

    def generateVelocity(self, distance): # Returns the calculated velocity based off of the distance, in inches.
        return 3622.819 * 1.0012328 ** distance

    def getRPM(self): # Returns the average RPM
        return (self.encoderOne.getVelocity() + self.encoderTwo.getVelocity()) / 2

