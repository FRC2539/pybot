import wpilib
import math
from ctre import ControlMode, FeedbackDevice

class Turret:

    turretMotor: object

    def setup(self):
        pass


    def setPosition(self):
        turretMotor.set(Controlmode.Position, 10)

    def rotate(self, speed):
        turretMotor.set(Controlmode.PercentOutput, speed)

    def stop(self):
        turretMotor.stopMotor()

    def execute(self):
        pass
