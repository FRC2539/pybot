from .debuggablesubsystem import DebuggableSubsystem

from wpilib import DigitalInput

import ports
import robot

from ctre import WPI_TalonSRX, ControlMode, NeutralMode
from rev import CANSparkMax, MotorType
import wpilib

import csv
import time

from ctre import WPI_TalonSRX, ControlMode, NeutralMode
from rev import CANSparkMax, MotorType
class Motors(DebuggableSubsystem):
    '''Describe what this subsystem does.'''
    # NOTE: The get() is inverted in DI/O
    def __init__(self):
        super().__init__('Motors')
        self.talon = WPI_TalonSRX(2)
        self.spark = CANSparkMax(1, MotorType.kBrushed)

        self.sparkEncoder = self.spark.getEncoder()

        self.talonSwitchForward = DigitalInput(0)
        self.talonSwitchReverse = DigitalInput(1)

        self.sparkSwitchForward = DigitalInput(2)
        self.sparkSwitchReverse = DigitalInput(3)

        self.talon.setNeutralMode(NeutralMode.Coast)
        self.talon.setSafetyEnabled(False)

        self.encoder = wpilib.DutyCycleEncoder(9)
        #self.log = open('log.csv', 'w')
        #self.logWriter = csv.writer(self.log, delimiter=',', quotechar = '"', quoting=csv.QUOTE_MINIMAL)


    def setMotors(self):
        percentsT = self.calcPercentsTal()
        percentsS = self.calcPercentsSpark()

        #print('Setting Percent Output Talon: ' + str(percentsT) + '.')

        if self.talonSwitchForward.get() and self.talonSwitchReverse.get():
            self.talon.stopMotor()
        elif not self.talonSwitchReverse.get():
            self.talon.set(ControlMode.PercentOutput, float(percentsT * -1))
        else:
            self.talon.set(ControlMode.PercentOutput, percentsT)

        if self.sparkSwitchForward.get() and self.sparkSwitchReverse.get():
            self.spark.stopMotor()
        elif not self.sparkSwitchReverse.get():
            self.spark.set(percentsS * -1)
        else:
            self.spark.set(percentsS)


    def calcPercentsTal(self):
        # MODIFY THIS AS NEEDED
        return float(robot.potentiometer.getReadingTalon()) # Assuming five is the max val and zero is the default for the potentiometer.

    def calcPercentsSpark(self):
        # MODIFY THIS AS NEEDED
        print('Reading: ' + str(robot.potentiometer.getReadingSpark()))
        return float(robot.potentiometer.getReadingSpark()) # Assuming five is the max val and zero is the default for the potentiometer.

    def initDefaultCommand(self):
        from commands.motors.defaultcommand import DefaultCommand

        self.setDefaultCommand(DefaultCommand())
