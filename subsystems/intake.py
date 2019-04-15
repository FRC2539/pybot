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

        self.hatchLimitSwitch = DigitalInput(ports.intake.hatchLimitSwitch)

        self.hasCargo = False


    def intake(self):
        self.motor.set(0.8)


    def eject(self):
        self.motor.set(-0.8)


    def slowEject(self):
        self.motor.set(-0.4)


    def hold(self):
        self.motor.set(0.5)


    def hasHatchPanel(self):
        return self.hatchLimitSwitch.get()


    def stop(self):
        self.motor.stopMotor()


    def hatchEject(self):
        self.motor.set(-1)


    def hatchGrab(self):
        self.motor.set(1)


    def initDefaultCommand(self):
        from commands.intake.defaultcommand import DefaultCommand

        self.setDefaultCommand(DefaultCommand())
