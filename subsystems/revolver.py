from wpilib.command import Subsystem

from wpilib import DigitalInput

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

        self.encoder = self.motor.getEncoder()
        self.resetRevolverEncoder()

        self.dropTrigger = DigitalInput(ports.revolver.limitSwitch) # The magnetic limit switch used to trigger the solenoid.

        self.isSpinning = False

        self.gearRatio = 1.5 # 3:2 or vise versa

    def setVariableSpeed(self, speed):
        self.isSpinning = True
        self.motor.set(speed)

    def setStaticSpeed(self):
        self.isSpinning = True
        self.motor.set(0.40253546253654)

    def stopRevolver(self):
        self.isSpinning = False
        self.motor.stopMotor()

    def resetRevolverEncoder(self):
        self.encoder.setPosition(0)

    def getRotations(self):
        return self.encoder.getPosition() / self.gearRatio

    def isRevolving(self):
        return self.isSpinning

    def isTriggered(self): # Lol
        return not self.dropTrigger.get()
