from wpilib.command.command import Command
from custom.config import Config
import math
import robot

from networktables import NetworkTables

class GoToTapeCommand(Command):

    def __init__(self, pipeID=1):
        super().__init__('Go To Tape')

        self.requires(robot.drivetrain)

        self.nt = NetworkTables.getTable('limelight')

        self.tape = Config('limelight/tv', 5)
        self.strafe = Config('limelight/tx', 0)
        self.distance = Config('limelight/ty', 0)

        self.tapeoffset = Config('DriveTrain/tapeoffset', 0)

        self.pipeID = pipeID

        self.drivePipeID = 0 # Make this your basic drive pipeline.

        self.x = 0
        self.y = 0
        self.rotate = 0

        self.speedBoost = Config('DriveTrain/tapespeedboost', 1)


    def initialize(self):

        self.nt.putNumber('pipeline', self.pipeID)

        self._finished = False

    def execute(self):
        print(self.tape.getValue())
        if self.tape.getValue() == 1:
            oX = self.strafe.getValue() - self.tapeoffset # 2.5
            oY = self.distance.getValue()


            self.y = ((oY * 9) / 60) * -1
            self.x = (oX * 8) / 100

            if abs(oX) < 15:
                self.x = math.copysign(self.x * 0.9, self.x)

            if abs(oX) < 4.5:
                self.x = math.copysign(self.x * 0.7, self.x)

            if abs(oX) < 2.5:
                self.x = math.copysign(self.x * 0.4, self.x)

            if abs(oX) < 0.5:
                self.x = 0

            if abs(oY) <= 2.0:
                self.y = math.copysign(self.y - (self.y * 0.25), self.y)

            self.rotate = self.x
            self.x = 0


            robot.drivetrain.move(self.x, self.y, self.rotate)

            if not self._finished:
                self._finished = (abs(oX - self.tapeoffset)) <= 2.0 and oY <= 1.0


        else:
            #robot.lights.solidRed()
            print('No vision target found!')
            robot.drivetrain.move(0, 0, 0)


    def isFinished(self):
        return self._finished


    def end(self):
        robot.drivetrain.move(0, 0, 0)

        self.nt.putNumber('pipeline', self.drivePipeID)
