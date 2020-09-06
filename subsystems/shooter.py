from wpilib.command import Subsystem

from .cougarsystem import *

from ctre import WPI_TalonFX, FeedbackDevice, ControlMode

import ports

class Shooter(CougarSystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Shooter')

        self.shooterMotorOne = WPI_TalonFX(ports.shooter.shooterMotorOneID)
        self.shooterMotorOne.configSelectedFeedbackSensor(FeedbackDevice.IntegratedSensor, 0, 0)

        self.shooterMotorTwo = WPI_TalonFX(ports.shooter.shooterMotorTwoID)
        self.shooterMotorTwo.configSelectedFeedbackSensor(FeedbackDevice.IntegratedSensor, 0, 0)

        self.shooterMotorOne.config_kF(0, 0.00019, 0)
        self.shooterMotorOne.config_kP(0, 0.001, 0)
        self.shooterMotorOne.config_kI(0, 0, 0)
        self.shooterMotorOne.config_kD(0, 0.0001, 0)
        self.shooterMotorOne.config_IntegralZone(0, 0, 0)

        self.shooterMotorOne.setInverted(True)
        self.shooterMotorTwo.setInverted(False)

        self.shooterMotorTwo.follow(self.shooterMotorOne) # True to invert the motor NOTE: Follow does not seem to work. REV sucks ngl.

        self.shooting = False

        self.maxVel = 5800 # Experimental velocities.
        self.minVel = 2800

    def setRPM(self, rpm):
        self.shooting = True
        self.shooterMotorOne.set(ControlMode.Velocity, self.rpmToSensor(-rpm))

    def setPercent(self, val):
        self.shooterMotorOne.set(ControlMode.PercentOutput, val)

    def reverseShooter(self):
        self.shooting = True
        self.shooterMotorOne.set(ControlMode.PercentOutput, -0.4)

    def stopShooter(self):
        self.shooterMotorOne.stopMotor()
        self.shooterMotorTwo.stopMotor()

        self.shooting = False
        
    def rpmToSensor(self, rpm):
        return (rpm * 2048) / 600
    
    def sensorToRPM(self, units):
        return (units * 600) / 2048

    def isShooting(self):
        return self.shooting

    def getRPM(self): # Returns the average RPM
        return (self.sensorToRPM(self.shooterMotorOne.getSelectedSensorVelocity()))
