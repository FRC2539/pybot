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

        self.shooterSpeed = Config('Shooter/speed')

        for motor in self.motors:
            motor.setSafetyEnabled(False)
            motor.enableBrakeMode(False)
            motor.reverseSensor(True)

        self.number = 5
        '''
        Subclasses should configure motors correctly and populate activeMotors.
        '''
        self.activeMotors = []
        self._configureMotors()
        for motor in self.activeMotors:
            motor.setControlMode(CANTalon.ControlMode.Speed)
            motor.setPID(Config('Shooter/Speed/P'), Config('Shooter/Speed/I'), Config('Shooter/Speed/D'), Config('Shooter/Speed/F'))
        self.boilerVision = NetworkTables.getTable('cameraTarget')


    def isVisible(self):
        return self.boilerVision.getBoolean('boilerVisible')

    def offsetFromTarget(self):
        return self.boilerVision.getValue('boilerCenter')

    def distanceToTarget(self):
        return self.boilerVision.getValue('boilerDistance')

    def setShooterSpeed(self, speed):
        self.shooterSpeed = speed

    def getShooterSpeed(self):

        if self.number == 0:
            self.number = 1
            error1 = self.activeMotors[0].getError()
            print(error1)
        self.number -= 1
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

