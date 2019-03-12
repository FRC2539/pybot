from wpilib.command.command import Command
from custom.config import Config
import math
import robot

class GoPastTapeCommand(Command):

    def __init__(self):
        super().__init__('Go Past Tape')

        self.requires(robot.drivetrain)

        self.tape = Config('limelight/tv', 0)
        self.y = 0.2
        self.originallyFieldOriented = True


    def initialize(self):
        self.originallyFieldOriented = robot.drivetrain.isFieldOriented

        if self.originallyFieldOriented:
            robot.drivetrain.toggleFieldOrientation()


    def execute(self):
        if self.tape.getValue() == 1:
            robot.drivetrain.move(0, self.y, 0)

        else:
            print('No vision target found!')
            robot.drivetrain.move(0, 0, 0)


    def end(self):
        robot.drivetrain.move(0, 0, 0)

        if self.originallyFieldOriented:
            robot.drivetrain.toggleFieldOrientation()
