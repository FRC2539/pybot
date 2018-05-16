from .debuggablesubsystem import DebuggableSubsystem
from wpilib.command.subsystem import Subsystem

from ctre import WPI_TalonSRX, ControlMode, NeutralMode
import ports


class Index(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Index')

        self.indexWheel = WPI_TalonSRX(ports.shooter.indexWheelID)
        self.indexWheel.setSafetyEnabled(False)
        self.indexWheel.setNeutralMode(NeutralMode.Brake)


    def initDefaultCommand(self):
        from commands.index.defaultcommand import DefaultCommand

        self.setDefaultCommand(DefaultCommand())


    def setIndex(self, speed):
        '''Set motors to the given speed'''
        self.indexWheel.set(ControlMode.PercentOutput, speed)

    def intake(self):
        self.setIndex(1)

    def shoot(self):
        self.setIndex(-1)

    def stop(self):
        self.setIndex(0)
