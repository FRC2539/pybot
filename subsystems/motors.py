from .debuggablesubsystem import DebuggableSubsystem

from wpilib import DigitalInput

import ports
import robot

from ctre import WPI_TalonSRX, ControlMode, NeutralMode
from rev import CANSparkMax, MotorType

class Motors(DebuggableSubsystem):
    '''Describe what this subsystem does.'''
    # NOTE: The get() is inverted in DI/O
    def __init__(self):
        super().__init__('Motors')
        self.talon = WPI_TalonSRX(2)
        self.spark = CANSparkMax(1, MotorType.kBrushless)

        self.talonReverseSwitch = DigitalInput(0)
        self.sparkReverseSwitch = DigitalInput(1)

        self.talonEnabled = DigitalInput(2)
        self.sparkEnabled = DigitalInput(3)

        self.talon.setNeutralMode(NeutralMode.Coast)
        self.talon.setSafetyEnabled(False)

    def setMotors(self):
        percents = self.calcPercents()

        print('Setting Percent Output: ' + str(percents) + '.')
        if not self.talonEnabled.get():
            if self.talonReverseSwitch.get():
                self.talon.set(ControlMode.PercentOutput, float(percents * -1))
            else:
                self.talon.set(ControlMode.PercentOutput, percents)


        if not self.sparkEnabled.get():
            if self.sparkReverseSwitch.get():
                self.spark.set(percents * -1)
            else:
                self.spark.set(percents)

        print('NO MOTORS ENABLED!')

    def calcPercents(self):
        # MODIFY THIS AS NEEDED
        print('Reading: ' + str(robot.potentiometer.getReading()))
        return float(robot.potentiometer.getReading()) # Assuming five is the max val and zero is the default for the potentiometer.

    def initDefaultCommand(self):
        from commands.motors.defaultcommand import DefaultCommand

        self.setDefaultCommand(DefaultCommand())
