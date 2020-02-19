from .debuggablesubsystem import DebuggableSubsystem

from wpilib import DigitalInput

import robot
import ports

from rev import CANSparkMax, ControlType, MotorType

from networktables import NetworkTables as nt

class Shooter(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Shooter')

        self.motor = CANSparkMax(ports.shooter.motorID, MotorType.kBrushless)
        self.encoder = self.motor.getEncoder()
        self.controller = self.motor.getPIDController()

        self.secondMotor = CANSparkMax(ports.shooter.motorTwoID, MotorType.kBrushless)
        self.secondEncoder = self.motor.getEncoder()
        self.secondController = self.motor.getPIDController()

        self.shooterSensor = DigitalInput(ports.shooter.shooterSensor)
        self.lastCheck = False

        self.table = nt.getTable('Shooter')

        self.ballCount = 5 #Config('
        #self.rpm = 6000 # Make NT value

        self.motor.setInverted(False)

        self.controller.setFF(0.000162, 0)
        self.controller.setP(0.0015, 0)
        self.controller.setI(0, 0)
        self.controller.setD(0, 0)
        self.controller.setIZone(0, 0)

        self.secondController.setFF(0.000162, 0)
        self.secondController.setP(0.0015, 0)
        self.secondController.setI(0, 0)
        self.secondController.setD(0, 0)
        self.secondController.setIZone(0, 0)

        self.secondMotor.follow(self.motor, True) # inverts it

        self.shooting = False

        self.zeroNetworkTables()

    def reverse(self):
        self.motor.set(-0.7)

    def runAtSpeed(self, percent):
        self.motor.set(percent)
        #self.secondMotor.set(percent)

    def shootBall(self):
        self.motor.set(0.6)
        #self.secondMotor.set(0.6)

    def stop(self):
        self.motor.stopMotor()
        #self.secondMotor.stopMotor()

    def updateCheck(self):
        self.lastCheck = self.shooterSensor.get()

    def monitorBalls(self):
        if self.shooterSensor.get() and not self.lastCheck: # is there something there that was not there last time?
            if self.ballCount != 0:
                self.ballCount -= 1
                self.table.putNumber('BallCount', self.ballCount)
            self.lastCheck = True
        elif not self.shooterSensor.get(): # no ball present
            self.lastCheck = False # nothing there

    def sensorCount(self):
        if not self.shooterSensor.get() and not self.shooting:
            robot.intake.ballCount -= 1
            self.shooting = True
        elif self.shooterSensor.get():
            self.shooting = False
        self.table.putNumber('BallCount', robot.intake.ballCount)

    def updateNetworkTables(self):
        avgVel = round(((self.encoder.getVelocity() + self.secondEncoder.getVelocity()) / 2), 2)
        self.table.putNumber('ShooterRPM', avgVel)

    def setGoalNetworkTables(self, rpm=3500):
        self.table.putNumber('DesiredShooterRPM', rpm)

    def zeroNetworkTables(self):
        self.table.putNumber('ShooterRPM', 0.00)
        self.table.putNumber('DesiredShooterRPM', 0.00)

    def getRPM(self):
        return ((self.encoder.getVelocity() + self.secondEncoder.getVelocity()) / 2)

    def setRPM(self, rpm):
        self.controller.setReference(float(rpm), ControlType.kVelocity, 0, 0)
        #self.secondController.setReference(float(rpm), ControlType.kVelocity, 0, 0)
