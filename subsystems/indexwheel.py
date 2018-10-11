from .debuggablesubsystem import DebuggableSubsystem
from wpilib.command.subsystem import Subsystem
from ctre import ControlMode, NeutralMode, WPI_TalonSRX
from wpilib.digitalinput import DigitalInput

import ports


class IndexWheel(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('IndexWheel')
        self.indexWheel = WPI_TalonSRX(ports.indexwheel.indexWheelMotorID)
        self.indexWheel.setSafetyEnabled(False)
        self.indexWheel.setInverted(True)

        # Might need to be False

    def set(self, speed):
        self.indexWheel.set(ControlMode.PercentOutput, speed)

    def stop(self):
        self.set(0)

    def forward(self):
        self.set(0.75)

    def slowForward(self):
        self.set(0.5)

    def reverse(self):
        self.set(-0.45)
