from wpilib.command import Subsystem

from .cougarsystem import *

from rev import CANSparkMax, IdleMode, MotorType, ControlType

import ports

class Shooter(Subsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Shooter')

        self.shooterMotorOne = CANSparkMax(ports.shooter.shooterMotorOneID, MotorType.kBrushless)
        self.encoderOne = self.shooterMotorOne.getEncoder()
        self.controllerOne = self.shooterMotorOne.getPIDController()

        self.shooterMotorTwo = CANSparkMax(ports.shooter.shooterMotorTwoID, MotorType.kBrushless)
        self.encoderTwo = self.shooterMotorTwo.getEncoder()
        self.controllerTwo = self.shooterMotorTwo.getPIDController()

        self.controllerOne.setFF(0.00017, 0)
        self.controllerOne.setP(0.00038, 0)
        self.controllerOne.setI(0, 0)
        self.controllerOne.setD(0.0001, 0)
        self.controllerOne.setIZone(0, 0)

        self.shooterMotorOne.setInverted(True)

        self.shooterMotorTwo.follow(self.shooterMotorOne, True) # True to invert the motor NOTE: Follow does not seem to work. REV sucks ngl.

        self.shooting = False

        self.maxVel = 5800 # Experimental velocities.
        self.minVel = 2800

    def setRPM(self, rpm):
        self.shooting = True
        self.controllerOne.setReference(-rpm, ControlType.kVelocity, 0, 0)

    def setPercent(self, val):
        self.shooterMotorOne.set(val)

    def reverseShooter(self):
        self.shooting = True
        self.shooterMotorOne.set(-0.4)

    def stopShooter(self):
        self.shooterMotorOne.stopMotor()
        self.shooterMotorTwo.stopMotor()

        self.shooting = False

    def isShooting(self):
        return self.shooting

    def generateVelocity(self, distance): # Returns the calculated velocity based off of the distance, in inches.
        return 3622.819 * 1.0012328 ** distance

    def getRPM(self): # Returns the average RPM
        return (self.encoderOne.getVelocity() + self.encoderTwo.getVelocity()) / 2
