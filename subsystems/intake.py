from wpilib.command import Subsystem

from .cougarsystem import *

from rev import CANSparkMax, ControlType, MotorType, IdleMode

import ports

class Intake(Subsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Intake')

        self.intakeMotor = CANSparkMax(ports.intake.motorID, MotorType.kBrushless) # Confirm the motor type!

        self.intakeMotor.setIdleMode(IdleMode.kBrake)
        self.intakeMotor.setInverted(False)

    def intakeBalls(self):
        self.intakeMotor.set(0.5)

    def outakeBalls(self):
        self.intakeMotor.set(-0.5)

    def kickBalls(self):
        self.intakeMotor.set(-0.1)

    def stopIntake(self):
        self.intakeMotor.stopMotor()
