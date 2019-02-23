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

        self.cargo = DigitalInput(ports.intake.lightSensor)

    def intake(self):
        self.motor.set(0.6)


    def eject(self):
        self.motor.set(-0.6)


    def slowEject(self):
        self.motor.set(-0.4)


    def stop(self):
        self.motor.stopMotor()


    def hasCargo(self):
        return self.cargo.get()


    def initDefaultCommand(self):
        from commands.intake.defaultcommand import DefaultCommand

        self.setDefaultCommand(DefaultCommand())
