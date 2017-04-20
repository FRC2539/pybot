from .debuggablesubsystem import DebuggableSubsystem
from ctre import CANTalon
from networktables import NetworkTables

from custom.config import Config
import ports

class Shooter(DebuggableSubsystem):
    '''
    A system designed for shooting balls into high boiler.
    '''

    def __init__(self):
        super().__init__('Shooter')

        self.motor = CANTalon(ports.shooter.motorID)
        self.motor.setSafetyEnabled(False)
        self.motor.enableBrakeMode(False)
        self.motor.reverseSensor(True)
        self.motor.configPeakOutputVoltage(12, 0)

        self.boilerVision = NetworkTables.getTable('cameraTarget')


    def isVisible(self):
        return self.boilerVision.getBoolean('boilerVisible')


    def offsetFromTarget(self):
        if not self.isVisible():
            return None

        return self.boilerVision.getValue('boilerCenter')


    def distanceToTarget(self):
        if not self.isVisible():
            return None

        return self.boilerVision.getValue('boilerDistance')


    def startShooting(self, speed):
        self.motor.setPID(
            Config('Shooter/Speed/P'),
            Config('Shooter/Speed/I'),
            Config('Shooter/Speed/D'),
            Config('Shooter/Speed/F')
        )

        self.motor.setControlMode(CANTalon.ControlMode.Speed)
        self.motor.clearIaccum()
        self.motor.set(speed)


    def isReadyToFire(self):
        if self.motor.getControlMode() != CANTalon.ControlMode.Speed:
            return False

        return abs(self.motor.getError()) < 100


    def stop(self):
        self.motor.setControlMode(CANTalon.ControlMode.PercentVbus)
        self.motor.set(0)
