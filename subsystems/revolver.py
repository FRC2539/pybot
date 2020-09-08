from wpilib.command import Subsystem

from wpilib import DigitalInput, I2C

from .cougarsystem import *

from rev import ControlType, CANSparkMax, MotorType, IdleMode
from rev.color import ColorSensorV3

import ports
import wpilib

class Revolver(CougarSystem):

    def __init__(self):
        super().__init__('Revolver')

        self.motor = CANSparkMax(ports.revolver.motorID, MotorType.kBrushless)
        self.encoder = self.motor.getEncoder()
        self.controller = self.motor.getPIDController()

        self.controller.setP(1, 0)
        self.controller.setI(0, 0)
        self.controller.setD(0.001, 0)
        self.controller.setFF(0.1, 0)
        self.controller.setIZone(0, 0)

        source_ = wpilib.DigitalInput(ports.revolver.absoluteThroughbore)
        self.tbEnc = wpilib.DutyCycle(source_)

        self.motor.setIdleMode(IdleMode.kBrake)

        self.motor.setClosedLoopRampRate(2)
        self.motor.setOpenLoopRampRate(2)

        self.resetRevolverEncoder()

        #self.dropTrigger = DigitalInput(ports.revolver.limitSwitch) # The magnetic limit switch used to trigger the solenoid.
        self.frontSensor = ColorSensorV3(I2C.Port.kOnboard)

        self.frontSensor.configureProximitySensor(ColorSensorV3.ProximityResolution.k11bit, ColorSensorV3.ProximityMeasurementRate.k100ms)

        self.holeLocations = [9, 81, 153, 225, 297]
        self.dropPositions = [317.5] # The middle of the drop zones. Zones must be five degrees wide.

        self.isSpinning = False

        self.gearRatio = 15 # 3:2 or vise versa

    def getPosition(self):
        return self.tbEnc.getOutput() * 360

    def setVariableSpeed(self, speed):
        self.isSpinning = True
        self.motor.set(speed)

    def setStaticSpeed(self):
        self.isSpinning = True
        self.motor.set(0.70253546253654)

    def stopRevolver(self):
        self.isSpinning = False
        self.motor.stopMotor()

    def isFrontEmpty(self):
        return (self.frontSensor.getProximity() <= 160)

    def inDropZone(self):
        return (315 <= self.getPosition() <= 320)

    def resetRevolverEncoder(self):
        self.encoder.setPosition(0)

    def getAbsolute(self):
        return abs((self.encoder.getPosition() / self.gearRatio) % 1) # 0 - 1 of where we are.

    def getRotations(self):
        return self.encoder.getPosition() / self.gearRatio

    def setPosition(self, pos):
        self.controller.setReference(pos * self.gearRatio, ControlType.kPosition, 0, 0)

    def atPosition(self, pos):
        return abs(self.getAbsolute() - pos) <= 0.05

    def atHole(self):
        for x in self.holeLocations:
            if abs(x - self.getPosition()) <= 3:
                return True

        return False

    def isRevolving(self):
        return self.isSpinning
