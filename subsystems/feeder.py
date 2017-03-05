from .debuggablesubsystem import DebuggableSubsystem
from ctre import CANTalon
from networktables import NetworkTable
from custom.config import Config
from wpilib.servo import Servo
import ports

class Feeder(DebuggableSubsystem):
    '''
    A subsystem designed for feeding balls to the shooter.
    '''

    def __init__(self):
        super().__init__('Feeder')

        self.gate = Servo(ports.feeder.gateID)
        """self.motors = [
            CANTalon(ports.feeder.motorID)
        ]

        self.motorVoltage = .9
        for motor in self.motors:
            motor.setSafetyEnabled(False)
            motor.enableBrakeMode(False)

        '''
        Subclasses should configure motors correctly and populate activeMotors.
        '''
        self.activeMotors = []
        self._configureMotors()
        for motor in self.activeMotors:
            motor.setControlMode(CANTalon.ControlMode.PercentVbus)"""

    """def isEmpty(self):
        return False
        #return ports.feeder.sensorID"""

    def open(self):
        self.gate.set(1)
    def close(self):
        self.gate.set(.8)
    """def _configureMotors(self):
        '''
        Make any necessary changes to the motors and define self.activeMotors.
        '''

        self.activeMotors = self.motors"""
