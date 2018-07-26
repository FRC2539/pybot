from .debuggablesubsystem import DebuggableSubsystem
from wpilib.digitalinput import DigitalInput

import ports
from ctre import WPI_TalonSRX


class Intake(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Intake')

        self.lightSensor = DigitalInput(ports.intake.lightSensorID)

        self.leftmainmotor = WPI_TalonSRX(ports.intake.leftmainmotor)
        self.leftmainmotor.setSafetyEnabled(False)

        self.rightmainmotor = WPI_TalonSRX(ports.intake.rightmainmotor)
        self.rightmainmotor.setSafetyEnabled(False)
        self.leftmainmotor.setInverted(True)

    def IntakePowerCube(self, speed):
        self.leftmainmotor.set(speed)
        self.rightmainmotor.set(speed)

    def isCubeInIntake(self):
            return not self.lightSensor.get()
