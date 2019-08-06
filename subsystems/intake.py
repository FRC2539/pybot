from .debuggablesubsystem import DebuggableSubsystem
from ctre import ControlMode, NeutralMode, WPI_TalonSRX
from wpilib import DigitalInput

import ports


class Intake(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Intake')

        self.motor = WPI_TalonSRX(ports.intake.motorID)
        self.motor.setNeutralMode(NeutralMode.Brake)
        self.motor.setSafetyEnabled(False)

        self.hasCargo = False


    def intake(self):
        self.motor.set(0.6)


    def eject(self):
        self.motor.set(-1)


    def slowEject(self):
        self.motor.set(-0.4)


    def hold(self):
        self.motor.set(0.2)


    def stop(self):
        self.motor.stopMotor()


    def initDefaultCommand(self):
        from commands.intake.defaultcommand import DefaultCommand

        self.setDefaultCommand(DefaultCommand())
