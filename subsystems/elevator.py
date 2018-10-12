from .debuggablesubsystem import DebuggableSubsystem
from wpilib.command.subsystem import Subsystem
from ctre import ControlMode, NeutralMode, WPI_TalonSRX
from wpilib.digitalinput import DigitalInput
from wpilib import Spark
import ports
#import wpilib

class Elevator(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Elevator')
        self.elevatorBelt = Spark(ports.elevator.elevatorBeltMotorID)
        self.elevatorBelt.setSafetyEnabled(False)
        self.elevatorBelt.setInverted(False)

        # setInverted might need to be False

        self.elevatorWheel = WPI_TalonSRX(ports.elevator.elevatorWheelMotorID)
        self.elevatorWheel.setSafetyEnabled(False)
        self.elevatorWheel.setInverted(True)

    def set(self, speed):
        self.elevatorBelt.set(speed)
        self.elevatorWheel.set(ControlMode.PercentOutput, speed)

    def slowElevate(self):
        self.set(0.5)

        # Change as needed after testing

    def fastElevate(self):
        self.set(1)

    def slowLower(self):
        self.set(-0.5)

    def fastLower(self):
        self.set(-1)

    def stop(self):
        self.set(0)
