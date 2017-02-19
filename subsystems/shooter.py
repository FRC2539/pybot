from .debuggablesubsystem import DebuggableSubsystem
from ctre import CANTalon
from networktables import NetworkTables

from custom.config import Config
import ports

class Shooter(DebuggableSubsystem):
    '''
    A system designed for shooting balls into high goal.
    '''

    def __init__(self):
        super().__init__('Shooter')

        self.motors = [
            CANTalon(ports.shooter.motorID)
        ]

        self.shooterSpeed = 0

        for motor in self.motors:
            motor.setSafetyEnabled(False)
            motor.enableBrakeMode(False)
            motor.reverseSensor(True)
            motor.configPeakOutputVoltage(12, 0)

        self.number = 5
        '''
        Subclasses should configure motors correctly and populate activeMotors.
        '''
        self.activeMotors = []
        self._configureMotors()
        for motor in self.activeMotors:
            motor.setControlMode(CANTalon.ControlMode.Speed)
            motor.setPID(Config('Shooter/Speed/P'), Config('Shooter/Speed/I'), Config('Shooter/Speed/D'), Config('Shooter/Speed/F'), profile=0)
        self.boilerVision = NetworkTables.getTable('cameraTarget')


    def isVisible(self):
        return self.boilerVision.getBoolean('boilerVisible')

    def offsetFromTarget(self):
        return self.boilerVision.getValue('boilerCenter')

    def distanceToTarget(self):
        return self.boilerVision.getValue('boilerDistance')

    def setShooterSpeed(self, speed):
        self.shooterSpeed = speed
        self.activeMotors[0].setPID(Config('Shooter/Speed/P'), Config('Shooter/Speed/I'), Config('Shooter/Speed/D'), Config('Shooter/Speed/F'), profile=0)

    def getShooterSpeed(self):

        if self.number == 0:
            self.number = 1
            error1 = self.activeMotors[0].getError()
            print("%s : %s" % (error1, self.activeMotors[0].getSpeed()))
        self.number -= 1
        return self.activeMotors[0].getSpeed()

    def startShooting(self):
        for motor in self.activeMotors:
            motor.setControlMode(CANTalon.ControlMode.Speed)
            motor.setProfile(0)
            motor.clearIaccum()
            motor.set(self.shooterSpeed)

    def stop(self):
        for motor in self.activeMotors:
            motor.setControlMode(CANTalon.ControlMode.PercentVbus)
            motor.set(0)

    def _configureMotors(self):
        '''
        Make any necessary changes to the motors and define self.activeMotors.
        '''
        self.activeMotors = self.motors

