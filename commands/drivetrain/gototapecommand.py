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
        #self.wantsHatch = not robot.hatch.hasHatchPanel()

        #if (not self.wantsHatch) and robot.elevator.getPosition() >= 10.0:
            #if (not self.wantsHatch) and robot.elevator.getPosition() >= 25.0:
            #if robot.elevator.getPosition() >= 25.0:

            #self.low = True
            #print("low camera, elev: "+ str(robot.elevator.getPosition()) + " arm: "+ str(robot.arm.getPosition()))
        #else:
        #print("standard camera")
        #print("have tape: " + str(self.tape.getValue())) #very necessary edit
        #print("standard camera, elev: "+ str(robot.elevator.getPosition()) + " arm: "+ str(robot.arm.getPosition()))

        #self.low = True

        self.nt.putNumber('pipeline', self.pipeID)

        self._finished = False

    def execute(self):
        #if not self.low:
        if self.tape.getValue() == 1:
            #print(self.distance.getValue())
            oX = self.strafe.getValue() - self.tapeoffset # 2.5
            oY = self.distance.getValue()

            #print('OG X ' + str(oX))
            #print('OG Y ' + str(oY))

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

            if abs(oY) <= 2.5:
                self.y = math.copysign(self.y - (self.y * 0.25), self.y)

            #print('x ' + str(self.x))
            #print('y ' + str(self.y))
            #print('rotate ' + str(self.rotate))

            # Takes away small y speed value based off of distance

            self.rotate = self.x
            self.x = 0



            robot.drivetrain.move(self.x, self.y, self.rotate)

            #self.x = math.copysign((oX * 4) / 100, oX)
            #self.y = math.copysign((oY * 6) / 100, oY)
            #self.rotate = self.x / 3

            #print("X0: " + str(self.x))
            #print("Y0: " + str(self.y))
            #print("rotate0: " + str(self.rotate))

            #if abs(self.x) > 0.35:
                #self.x = math.copysign(0.35, self.x)
                #self.rotate = self.x / 3
            #elif abs(oX) <= 1.0:
                #self.x = oX / 10.0
                #self.rotate = self.x / 2.0
            #elif abs(oX) > 1.0 and abs(self.x) < 0.2:
                #self.x = math.copysign(0.2, oX)
                #self.rotate = math.copysign(0.1, oX) / 2.0

            #print("X1: " + str(self.x))
            #print("Y1: " + str(self.y))
            #print("rotate1: " + str(self.rotate))

            #if self.y > 0.50:
               #self.y = 0.50
            #elif oY <= 0.0:
                #self.y = 0
            #elif oY > 0.0 and self.y < 0.3:
                #self.y = 0.3

            #print("X2: " + str(self.x))
            #print("Y2: " + str(self.y))
            #print("rotate2: " + str(self.rotate))

            #if abs(oY) <= 4.0:
                #self.rotate = self.rotate * 0.5

            #if abs(oY) <= 2.0:
                #self.y = 0.1

            #if abs(oY) <= 3.5:
                #self.y = 0.15

            #print("X3: " + str(self.x))
            #print("Y3: " + str(self.y))
            #print("rotate3: " + str(self.rotate))

            #self.y = self.y * self.speedBoost

            #self.y = 0

           # robot.drivetrain.move(self.x, self.y, self.rotate)


            #if self.wantsHatch:
            #    self._finished = robot.hatch.hasHatchPanel()

            if not self._finished:
                #self._finished = (abs(self.x) <= 0.03 and abs(self.y) <= 0.03 and abs(self.rotate) <= 0.03) or oY <= 1.0
                self._finished = (abs(oX - self.tapeoffset)) <= 2.0 and oY <= 1.0


            #if self._finished:
                #robot.lights.solidGreen()
            #else:
                #robot.lights.solidBlue()

        else:
            #robot.lights.solidRed()
            print('No vision target found!')
            robot.drivetrain.move(0, 0, 0)


    def isFinished(self):
        return self._finished


    def end(self):
        robot.drivetrain.move(0, 0, 0)

        self.nt.putNumber('pipeline', self.drivePipeID)
