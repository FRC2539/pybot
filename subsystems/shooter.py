from wpilib.command.subsystem import Subsystem

from ctre import WPI_TalonSRX, ControlMode, NeutralMode
import ports
from custom.config import Config

class Shooter(Subsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Shooter')

        self.left = WPI_TalonSRX(ports.shooter.leftPivotMotorID)
        self.right = WPI_TalonSRX(ports.shooter.rightPivotMotorID)
        self.left.setNeutralMode(NeutralMode.Brake)
        self.right.setNeutralMode(NeutralMode.Brake)
        self.left.setSafetyEnabled(False)
        self.left.setSafetyEnabled(False)
        self.right.setInverted(True)


    def initDefaultCommand(self):
        from commands.shooter.defaultcommand import DefaultCommand

        self.setDefaultCommand(DefaultCommand())


    def set(self, speed):
        self.left.set(ControlMode.PercentOutput, speed)
        self.right.set(ControlMode.PercentOutput, speed)

    def up(self):
        self.set(1)


    def down(self):
        self.set(-0.5)

    def stop(self):
        self.set(0)
