from .debuggablesubsystem import DebuggableSubsystem
from ctre import CANTalon
from networktables import NetworkTable

from custom.config import Config
import ports

class Climbing(DebuggableSubsystem):
    '''
    A subsystem designed for picking up balls from the floor.
    '''

    def __init__(self):
        super().__init__('Climbing')

        self.motors = [
            CANTalon(ports.climbing.motorID)
        ]

        self.motorVoltage = .7

        for motor in self.motors:
            motor.setSafetyEnabled(False)
            motor.enableBrakeMode(False)

        '''
        Subclasses should configure motors correctly and populate activeMotors.
        '''
        self.activeMotors = []
        self._configureMotors()
        for motor in self.activeMotors:
            motor.setControlMode(CANTalon.ControlMode.PercentVbus)

    def startClimbing(self):
        for motor in self.activeMotors:
            motor.set(self.motorVoltage)
    def stop(self):
        for motor in self.activeMotors:
            motor.set(0)
    def _configureMotors(self):
        '''
        Make any necessary changes to the motors and define self.activeMotors.
        '''

        self.activeMotors = self.motors
