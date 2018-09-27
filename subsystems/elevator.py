from .debuggablesubsystem import DebuggableSubsystem
from wpilib.command.subsystem import Subsystem
import ports
from ctre import WPI_TalonSRX, ControlMode, FeedbackDevice
import threading

class Elevator(DebuggableSubsystem):
    '''For lifting and lowering elevator'''

    def __init__(self):
        super().__init__('Elevator')

        self.motor = WPI_TalonSRX(ports.elevator.motorID)
        self.motor.setSafetyEnabled(False)

        self.lowerlimit = 0
        self.upperlimit = 10000
        self.motor.configForwardSoftLimitEnable(True, 0)
        self.motor.configReverseSoftLimitEnable(True, 0)
        self.motor.configMotionAcceleration(2000, 0)
        self.motor.configMotionCruiseVelocity(870, 0)
        self.motor.configPeakCurrentLimit(40, 0)
        self.motor.configPeakCurrentDuration(100, 0)
        self.motor.configReverseSoftLimitThreshold(self.lowerlimit, 0)
        self.motor.configForwardSoftLimitThreshold(self.upperlimit, 0)



    def set(self, speed):
        self.motor.set(ControlMode.PercentOutput, speed)

    def getHeight(self):
        return self.motor.getSelectedSensorPosition(0)

    def reset(self):
        self.motor.setSelectedSensorPosition(0, 0, 0)

    def up(self):
        self.set(0.75)

    def down(self):
        self.set(-0.5)

    def stop(self):
        self.set(0)

    def enableLowerLimit(self, enable):
        self.motor.configReverseSoftLimitEnable(True, 0)

    def goToHeight(self, height):
        self.motor.set(ControlMode.MotionMagic, height)

    def getSpeed(self):
        return abs(self.motor.getQuadratureVelocity())
