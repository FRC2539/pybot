from .debuggablesubsystem import DebuggableSubsystem
from ctre import ControlMode, NeutralMode, WPI_TalonSRX
from wpilib import DigitalInput

import ports


class Hatch(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Hatch')

        self.motor = WPI_TalonSRX(ports.hatch.motorID)
        self.motor.setNeutralMode(NeutralMode.Brake)
        self.motor.setSafetyEnabled(False)

        self.limitSwitch = DigitalInput(ports.hatch.limitSwitch)

        self.hasHatch = False


    def hold(self):
        self.motor.set(0.5)


    def hasHatchPanel(self):
        return not self.limitSwitch.get()


    def stop(self):
        self.motor.set(0)


    def eject(self):
        self.motor.set(-1)


    def grab(self):
        self.motor.set(1)


    def initDefaultCommand(self):
        from commands.hatch.defaultcommand import DefaultCommand

        self.setDefaultCommand(DefaultCommand())
