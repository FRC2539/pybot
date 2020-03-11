import wpilib
import math
from rev import CANSparkMax, MotorType, ControlType
from custom.config import Config

class Hood:

    hoodMotor: object
    hoodEncoder: object

    hoodMax: float
    hoodMin: float

    def setup(self):
        self.PIDController = self.hoodMotor.getPIDController()

        self.PIDController.setFF(0.0001 ,0)
        self.PIDController.setP(0.0001 ,0)
        self.PIDController.setI(0 ,0)
        self.PIDController.setD(0.0001 ,0)
        self.PIDController.setIZone(0 ,0)

    def setAngle(self, angle):
        self.target = angle
        self.PIDController.setReference(float(self.target), ControlType.kPosition, 0, 0)

    def runHood(self, speed):
        self.hoodMotor.set(speed)

    def getPosition(self):
        return self.hoodEncoder.getOutput() * 360

    def execute(self):
        if not self.hoodMin < self.getPosition() < self.hoodMax:
            self.hoodMotor.stopMotor()
