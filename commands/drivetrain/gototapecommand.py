from wpilib.command.command import Command
from custom.config import Config
import math
import robot

from networktables import NetworkTables

class GoToTapeCommand(Command):

    def __init__(self, pipeID=0):
        super().__init__('Go To Tape')

        self.requires(robot.drivetrain)

        self.tape = Config('limelight/tv', 0)
        self.strafe = Config('limelight/tx', 0)
        self.distance = Config('limelight/ty', 0)

        self.nt = NetworkTables.getTable('limelight')

        self.pipeID = pipeID

        self.drivePipeID = 0 # Make this your basic drive pipeline.

        self.x = 0
        self.y = 0
        self.rotate = 0

        self.fineRotate = 0.75
        self.fineStrafe = 0.50
        self.fineMove = 0.85

        self.originallyFieldOriented = True


    def initialize(self):
        self.nt.putNumber('ledMode', 3)

        self.originallyFieldOriented = robot.drivetrain.isFieldOriented

        if self.originallyFieldOriented:
            robot.drivetrain.toggleFieldOrientation()

        self.nt.putNumber('pipeline', self.pipeID)

        self._finished = False

    def execute(self):
        #old
        if self.tape.getValue() == 1:
            oX = self.strafe.getValue() + 3.5 #Adjust for off center camera position
            oY = self.distance.getValue()

            self.x = math.copysign((oX * 4) / 100, oX)
            self.y = math.copysign((oY * 6) / 100, oY)
            self.rotate = self.x / 3

            if abs(self.x) > 0.35:
                self.x = math.copysign(0.35, self.x)
                self.rotate = self.x / 3
            elif abs(oX) <= 1.0:
                self.x = oX / 10.0
                self.rotate = self.x / 2.0
            elif abs(oX) > 1.0 and abs(self.x) < 0.2:
                self.x = math.copysign(0.2, oX)
                self.rotate = math.copysign(0.1, oX) / 2.0

            if self.y > 0.40:
                self.y = 0.40
            elif oY <= 0.0:
                self.y = 0
            elif oY > 0.0 and self.y < 0.3:
                self.y = 0.3

            if oY <= 4.0:
                self.rotate = 0.0

            if oY <= 2.0:
                self.y = 0.1
            elif oY <= 3.5:
                self.y = 0.15



            robot.drivetrain.move(self.x, self.y, self.rotate)

            self._finished = (abs(self.x) <= 0.03 and abs(self.y) <= 0.03 and abs(self.rotate) <= 0.03) or oY <= 0.25

            if self._finished:
                robot.lights.solidGreen()
            else:
                robot.lights.solidPurple()

        else:
            robot.lights.solidRed()
            print('No vision target found!')
            robot.drivetrain.move(0, 0, 0)

        ################################################3
        #__new__


        #if self.tape.getValue() == 1:
            #oX = self.strafe.getValue() + 1.0 #Adjust for off center camera position
            #oY = self.distance.getValue()

            #self.x = math.copysign((oX * 3) / 100, oX)
            #self.y = math.copysign((oY * 3) / 100, oY)
            #self.rotate = self.x / 2


            #if self.x > 0.4:
                #self.x = math.copysign(0.4, self.x)
                #self.rotate = self.x
            #elif abs(oX) <= 0.5:
                #self.x = oX / 5
                #self.rotate = self.x
            #elif abs(oX) > 0.5 and self.x < 0.1:
                #self.x = math.copysign(0.23, oX)
                #self.rotate = math.copysign(0.12, oX)

            ##if self.y > 0.45:
             ##   self.y = 0.5
            #if oY < 2.5:
                #self.y = 0.15
            #elif oY < 0.0:
                #self.y = 0
            #elif oY > 0.8 and self.y < 0.15:
                #self.y = 0.2
            #elif oY > 4.5:
                #print('running bens stuff')
                #self.y = 0.6

            #self.nx = self.x * self.fineStrafe
            #self.nRotate = self.rotate * self.fineRotate
            #self.ny = self.y * self.fineMove

            #robot.drivetrain.move(self.nx, self.ny, self.nRotate)

            #self._finished = (abs(self.x) <= 0.02 and abs(self.y) <= 0.02 and abs(self.rotate) <= 0.02) or oY <= 0.25

            #if self._finished:
                #robot.lights.solidGreen()
            #else:
                #robot.lights.solidPurple()

        #else:
            #robot.lights.solidRed()
            #print('No vision target found!')
            #robot.drivetrain.move(0, 0, 0)


    def isFinished(self):
        return self._finished


    def end(self):
        robot.drivetrain.move(0, 0, 0)

        self.nt.putNumber('pipeline', self.drivePipeID)

        if self.originallyFieldOriented:
            robot.drivetrain.toggleFieldOrientation()

        self.nt.putNumber('ledMode', 1)

        robot.lights.off()
