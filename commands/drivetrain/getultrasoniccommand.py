from wpilib.command import Command
from custom.analogultrasonic import AnalogUltrasonic
from networktables import NetworkTables
from wpilib.analoginput import AnalogInput

import ports


class GetUltrasonicCommand(Command):

    def __init__(self):
        super().__init__('GetUltrasonic')

        self.ultrasonic = AnalogInput(ports.drivetrain.ultrasonicSensorID)

    def initialize(self):
        return self.ultrasonic.getAverageVoltage()
