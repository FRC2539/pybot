from wpilib.command import Subsystem

from .cougarsystem import *

from rev import ControlType, CANSparkMax, MotorType, IdleMode

import ports

class Revolver(Subsystem):

    def __init__(self):
        super().__init__('Revolver')

        self.motor = CANSparkMax(ports.revolver.motorID, MotorType.kBrushless)

        self.motor.setIdleMode(IdleMode.kBrake)

        self.motor.setClosedLoopRampRate(2)
        self.motor.setOpenLoopRampRate(2)

    def setVariableSpeed(self, speed):
        self.motor.set(speed)

    def setStaticSpeed(self):
        self.motor.set(0.30253546253654)

    def stopRevolver(self):
        self.motor.stopMotor()
