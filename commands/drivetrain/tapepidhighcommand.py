from wpilib.command.command import Command
from custom.config import Config
import math
import robot

from networktables import NetworkTables

class tapePIDHighCommand(Command):

    def __init__(self):
        super().__init__('tape P I D High')

        self.requires(robot.drivetrain)


    def initialize(self):
        pass


    def execute(self):
        pass


    def end(self):
        pass
