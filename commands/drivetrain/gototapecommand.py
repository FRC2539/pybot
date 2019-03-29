from wpilib.command.command import Command
from custom.config import Config
import math
import robot

from networktables import NetworkTables

class GoToTapeCommand(Command):

    def __init__(self):
        super().__init__('Go To Tape')

        self.requires(robot.drivetrain)

        self.tape = Config('limelight/tv', 0)
        self.strafe = Config('limelight/tx', 0)
        self.distance = Config('limelight/ty', 0)

        self.nt = NetworkTables.getTable('limelight')

        self.x = 0
        self.y = 0
        self.rotate = 0

        self.originallyFieldOriented = True


    def initialize(self):
        self.nt.putNumber('ledMode', 3)

        self.originallyFieldOriented = robot.drivetrain.isFieldOriented

        if self.originallyFieldOriented:
            robot.drivetrain.toggleFieldOrientation()

        self._finished = False


    def execute(self):
        if self.tape.getValue() == 1:
            self.x = self.strafe.getValue() + 1.5 #Adjust for off center camera position
            self.y = self.distance.getValue()

            oY = self.y
            oX = self.x

            self.x = math.copysign((self.x * 3) / 100, self.x)
            self.y = math.copysign((self.y * 3) / 100, self.y)
            self.rotate = self.x / 2


            if self.x > 0.4:
                self.x = math.copysign(0.4, self.x)
                self.rotate = self.x
            elif abs(oX) <= 0.5:
                self.x = oX / 5
                self.rotate = self.x
            elif abs(oX) > 0.5 and self.x < 0.1:
                self.x = math.copysign(0.1, oX)
                self.rotate = math.copysign(0.1, oX)

            if self.y > 0.45:
                self.y = 0.45
            elif oY < 0.0:
                self.y = 0
            elif oY > 0.5 and self.y < 0.15:
                self.y = 0.15


            robot.drivetrain.move(self.x, self.y, self.rotate)

            self._finished = (abs(self.x) <= 0.02 and abs(self.y) <= 0.02 and abs(self.rotate) <= 0.02) or oY <= 0.25

            if self._finished:
                robot.lights.solidGreen()
            else:
                robot.lights.solidPurple()

        else:
            robot.lights.solidRed()
            print('No vision target found!')
            robot.drivetrain.move(0, 0, 0)


    def isFinished(self):
        return self._finished


    def end(self):
        robot.drivetrain.move(0, 0, 0)

        if self.originallyFieldOriented:
            robot.drivetrain.toggleFieldOrientation()

        self.nt.putNumber('ledMode', 1)

        robot.lights.off()
