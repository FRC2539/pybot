from .debuggablesubsystem import DebuggableSubsystem

import ports
import wpilib

from rev import CANSparkMax, MotorType, ControlType
from custom.config import Config


class Hood(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Hood')

        self.motor = CANSparkMax(ports.hood.motorID, MotorType.kBrushless)
        self.encoder = self.motor.getEncoder()
        self.controller = self.motor.getPIDController()

        self.controller.setFF(0.00019 , 0)
        self.controller.setP(0.0001 , 0)
        self.controller.setI(0 , 0)
        self.controller.setD(0.001 , 0)
        self.controller.setIZone(0 , 0)

        source_ = wpilib.DigitalInput(9)
        self.tbEnc = wpilib.DutyCycle(source_)

        self.angleMax = 155 # NOTE DO not actually make this 0 and 90. Place-holder only; make like 20, 110
        self.angleMin = 85

    def getPosition(self):
        return self.tbEnc.getOutput() * 360

    def setAngle(self, angle):
        self.controller.setReference(float(angle), ControlType.kPosition, 0 , 0)

    def stopHood(self):
        self.motor.stopMotor()

    def raiseHood(self):
        if self.getPosition() < self.angleMax:
            self.motor.set(0.4)
        else:
            self.motor.stopMotor()
            print('\n\n\nMAXED OUT\n\n\n')

    def lowerHood(self):
        if self.getPosition() > self.angleMin:
            self.motor.set(-0.4)
        else:
            self.motor.stopMotor()
            print('\n\n\nMIN REACHED\n\n\n')

    def atHighest(self):
        if self.getPosition() >= self.angleMax:
            self.motor.stopMotor()
            return True
        else:
            return False

    def atLowest(self):
        if self.getPosition() <=  self.angleMin:
            self.motor.stopMotor()
            return True
        else:
            return False

    def initDefaultCommand(self):
        from commands.hood.defaultcommand import DefaultCommand

        self.setDefaultCommand(DefaultCommand())
