from wpilib.command import Subsystem

from .cougarsystem import *

from rev import CANSparkMax, ControlType, MotorType, IdleMode

import ports

class Intake(CougarSystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Intake')

        self.intakeMotor = CANSparkMax(ports.intake.motorID, MotorType.kBrushless) # Confirm the motor type!

        self.intakeMotor.setIdleMode(IdleMode.kBrake)
        self.intakeMotor.setInverted(True)

        self.intakeMotor.burnFlash()
        
        self.intaking = False
        
        disablePrints()

    def intakeBalls(self):
        self.intaking = True
        self.intakeMotor.set(0.5)

    def outakeBalls(self):
        self.intaking = False
        self.intakeMotor.set(-0.5)

    def kickBalls(self):
        self.intaking = False
        self.intakeMotor.set(-0.1)

    def stopIntake(self):
        self.intaking = False
        self.intakeMotor.stopMotor()
