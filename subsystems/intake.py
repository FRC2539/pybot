from wpilib.command.subsystem import Subsystem

from ctre import WPI_TalonSRX, ControlMode, NeutralMode
import ports
from wpilib.digitalinput import DigitalInput

class Intake(Subsystem):
    '''A set of parallel conveyors that will collect and eject power cubes.'''

    def __init__(self):
        super().__init__('Intake')

        self.leftMotor = WPI_TalonSRX(ports.shooter.indexWheelID)
        self.leftMotor.setSafetyEnabled(False)
        self.leftMotor.setNeutralMode(NeutralMode.Brake)
        self.leftMotor.setInverted(True)

        self.rightMotor = WPI_TalonSRX(ports.shooter.shooterWheelID)
        self.rightMotor.setSafetyEnabled(False)
        self.rightMotor.setNeutralMode(NeutralMode.Brake)


    def initDefaultCommand(self):
        from commands.intake.defaultcommand import DefaultCommand

        self.setDefaultCommand(DefaultCommand())


    def set(self, speed):
        '''Set motors to the given speed'''
        self.leftMotor.set(ControlMode.PercentOutput, speed)
        self.rightMotor.set(ControlMode.PercentOutput, speed)


    def intake(self):
        self.set(1)


    def outtake(self):
        self.set(-1)


    def stopTake(self):
        self.set(0)
