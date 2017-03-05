from .debuggablesubsystem import DebuggableSubsystem
from ctre import CANTalon
from networktables import NetworkTable

from custom.config import Config
import ports

class Pickup(DebuggableSubsystem):
    '''
    A subsystem designed for picking up balls from the floor.
    '''

    def __init__(self):
        super().__init__('Pickup')

        self.motors = [
            CANTalon(ports.pickup.motorID)
        ]

        self.motorVoltage = .9

        for motor in self.motors:
            motor.setSafetyEnabled(False)
            motor.enableBrakeMode(False)
            motor.setInverted(True)

        '''
        Subclasses should configure motors correctly and populate activeMotors.
        '''
        self.activeMotors = []
        self._configureMotors()
        for motor in self.activeMotors:
            motor.setControlMode(CANTalon.ControlMode.PercentVbus)

    def startBallPickup(self):
        for motor in self.activeMotors:
            motor.set(self.motorVoltage)

    def reverseBallPickup(self):
        for motor in self.activeMotors:
            motor.set(-self.motorVoltage)
    def stop(self):
        for motor in self.activeMotors:
            motor.set(0)
    def _configureMotors(self):
        '''
        Make any necessary changes to the motors and define self.activeMotors.
        '''

        self.activeMotors = self.motors
