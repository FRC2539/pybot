from wpilib.command.command import Command
from custom.config import Config
import math
import robot

from networktables import NetworkTables

class TapePIDCommand(Command):

    def __init__(self):
        super().__init__('Tape P I D')

        self.requires(robot.drivetrain)


    def initialize(self):
        pass


    def execute(self):
        pass


    def end(self):
        pass
