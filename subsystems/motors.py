from .debuggablesubsystem import DebuggableSubsystem

import ports
import robot

from ctre import WPI_TalonSRX, ControlMode, NeutralMode
from rev import CANSparkMax, MotorType

class Motors(DebuggableSubsystem):
    '''Describe what this subsystem does.'''

    def __init__(self):
        super().__init__('Motors')
        self.talon = WPI_TalonSRX(2)
        self.spark = CANSparkMax(1, MotorType.kBrushless)

        self.talon.setNeutralMode(NeutralMode.Coast)
        self.talon.setSafetyEnabled(False)

    def setMotors(self):
        percents = self.calcPercents()

        print('Setting Percent Output: ' + str(percents) + '.')

        self.talon.set(ControlMode.PercentOutput, percents)
        self.spark.set(percents)

    def calcPercents(self):
        # MODIFY THIS AS NEEDED
        print('Reading: ' + str(robot.potentiometer.getReading()))
        return float(robot.potentiometer.getReading()) # Assuming five is the max val and zero is the default for the potentiometer.

    def initDefaultCommand(self):
        from commands.motors.defaultcommand import DefaultCommand

        self.setDefaultCommand(DefaultCommand())
