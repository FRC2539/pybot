import wpilib
import math
from rev import CANSparkMax, MotorType, ControlType
from custom.config import Config

class Hood:

    hoodMotor: object

    def setup(self):
        self.PIDController = self.hoodMotor.getPIDController()

        self.PIDController.setFF(0.0001 ,0)
        self.PIDController.setP(0.0001 ,0)
        self.PIDController.setI(0 ,0)
        self.PIDController.setD(0.0001 ,0)
        self.PIDController.setIZone(0 ,0)


        self.encoder =wpilib.DutyCycleEncoder(9)


    def setAngle(self, angle):
        self.target = angle
        self.PIDController.setReference(float(self.target), ControlType.kPosition, 0, 0)

    def execute(self):
        print(self.encoder.getDistance())
