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

    def getEnc(self):
        #print('enc degrees ' + str(self.tbEnc.getOutput() * 360))
        pass

    def setAngle(self, angle):
        self.controller.setReference(float(angle), ControlType.kPosition, 0 , 0)


    def initDefaultCommand(self):
        from commands.hood.defaultcommand import DefaultCommand

        self.setDefaultCommand(DefaultCommand())
