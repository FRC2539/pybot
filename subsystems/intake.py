from wpilib.command.subsystem import Subsystem

from ctre import WPI_TalonSRX, ControlMode, NeutralMode
import ports
from wpilib.digitalinput import DigitalInput

class Intake(Subsystem):
    '''A set of parallel conveyors that will collect and eject power cubes.'''

    def __init__(self):
        super().__init__('Intake')

        self.shooterWheel = WPI_TalonSRX(ports.shooter.shooterWheelID)
        self.shooterWheel.setSafetyEnabled(False)
        self.shooterWheel.setNeutralMode(NeutralMode.Brake)


    def initDefaultCommand(self):
        from commands.intake.defaultcommand import DefaultCommand

        self.setDefaultCommand(DefaultCommand())


    def setShoot(self, speed):
        '''Set motors to the given speed'''
        self.shooterWheel.set(ControlMode.PercentOutput, speed)

    def intake(self):
        self.setShoot(1)


    def outtake(self):
        self.setShoot(-1)


    def stop(self):
        self.setShoot(0)
