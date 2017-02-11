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

        self.shooterSpeed = 10000

        for motor in self.motors:
            motor.setSafetyEnabled(False)
            motor.enableBrakeMode(False)

        '''
        Subclasses should configure motors correctly and populate activeMotors.
        '''
        self.activeMotors = []
        self._configureMotors()
        for motor in self.activeMotors:
            motor.setControlMode(CANTalon.ControlMode.Speed)
            motor.setPID(0, 0, 0, .9)

        self.boilerVision = NetworkTables.getTable('cameraTarget')


    def IsTargetVisible(self):
        return self.boilerVision.getBoolean('boilerVisible')

    def offsetFromTarget(self):
        return self.boilerVision.getValue('boilerCenter')

    def distanceToTarget(self):
        return self.boilerVision.getValue('boilerDistance')

    def setShooterSpeed(self, speed):
        self.shooterSpeed = speed

    def getShooterSpeed(self):
        return self.activeMotors[0].getSpeed()

    def startShooting(self):
        for motor in self.activeMotors:
            motor.setControlMode(CANTalon.ControlMode.Speed)
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

