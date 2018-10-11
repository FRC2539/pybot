from .debuggablesubsystem import DebuggableSubsystem
from wpilib.command.subsystem import Subsystem
from ctre import ControlMode, NeutralMode, WPI_TalonSRX
from wpilib.digitalinput import DigitalInput
from wpilib import PWMSpeedController

import ports


class Shooter(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Shooter')
        self.shooter = WPI_TalonSRX(ports.shooter.shooterMotorID)
        self.shooter.setSafetyEnabled(False)
        self.shooter.setInverted(True)

        # setInverted might need to be False

    def set(self, speed):
        self.shooter.set(ControlMode.PercentOutput, speed)

    def shoot(self):
        self.set(1)

    def slowShoot(self):
        self.set(0.75)

        # Adjust speed values

    def stop(self):
        self.set(0)
