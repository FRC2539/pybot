from wpilib.command.subsystem import Subsystem
from ctre import WPI_TalonSRX, ControlMode
from networktables import NetworkTables

from custom.config import Config
import ports

class Shooter(Subsystem):
    '''
    A system designed for shooting balls into high boiler.
    '''

    def __init__(self):
        super().__init__('Shooter')

        self.motor = WPI_TalonSRX(ports.shooter.motorID)
        self.motor.setSafetyEnabled(False)
        self.motor.setNeutralMode(False)
        self.motor.setInverted(False)
        self.motor.configPeakOutputReverse(-1, 0)

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
        self.motor.config_kP(0, 0, 0)
        self.motor.config_kI(0, 0, 0)
        self.motor.config_kD(0, 0, 0)
        self.motor.config_kF(0, 0.7, 0)


        self.motor.set(ControlMode.Velocity, speed)
        self.motor.setIntegralAccumulator(0, 0, 0)


    def isReadyToFire(self):
        #if self.motor.getControlMode() != ControlMode.Velocity:
            #return False

        return True #abs(self.motor.getClosedLoopError(0)) < 100


    def stop(self):
        self.motor.set(ControlMode.PercentOutput, 0)
