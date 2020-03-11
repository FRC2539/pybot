import wpilib
import math
from ctre import ControlMode, FeedbackDevice

class Turret:

    turretMotor: object

    def setup(self):
        pass


    def setPosition(self):
        self.turretMotor.set(Controlmode.Position, 10)

    def rotate(self, speed):
        self.turretMotor.set(Controlmode.PercentOutput, speed)

    def stop(self):
        self.turretMotor.stopMotor()

    def execute(self):
        pass
