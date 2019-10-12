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
            theta = math.radians(oY+79.9)

            oD = 2.5 * math.tan(theta)
            oD = oD - 14
            #oD = abs(oD)


            if abs(oX) > 10 :
                self.rotate = math.copysign(.30,oX)
            elif abs(oX) > 5 :
                self.rotate = math.copysign(.25, oX)
            elif abs(oX) > 3 :
                self.rotate = math.copysign(.20, oX)
            elif abs(oX) > 1 :
                self.rotate = math.copysign(.15, oX)
            else:
                self.rotate = 0


            #if oD > 36 :
                #self.y = .30
            #elif oD > 24 :
                #self.y = .25
            #elif oD > 12 :
                #self.y = .20
            #else:
                #self.y = .15

            #self.y = self.y * self.speedBoost

            #if self.y < .15:
                #self.y = .15

            self.y = (oD*oD)/5000 + .15


            #self.y = ((oY * 9) / 60) * -1
            #self.x = (oX * 8) / 100

            #if abs(oX) < 15:
                #self.x = math.copysign(self.x * 0.9, self.x)

            #if abs(oX) < 4.5:
                #self.x = math.copysign(self.x * 0.7, self.x)

            #if abs(oX) < 2.5:
                #self.x = math.copysign(self.x * 0.4, self.x)

            #if abs(oX) < 0.5:
                #self.x = 0

            #if abs(oY) <= 1.0:
                #self.y = (oY * oY) * -1#math.copysign(self.y - (self.y * 0.25), self.y)

            #self.rotate = self.x /3
            #self.x = 0

            #self.y = self.y * self.speedBoost.getValue()

            self.x = 0
            self.rotate = self.rotate

            robot.drivetrain.move(self.x, self.y, self.rotate)

            print('oy = ' + str(oY) + " od = "+ str(oD))
            if not self._finished:
                self._finished = oD <= 0.390
                #self._finished = oY <= .5


        else:
            #robot.lights.solidRed()
            print('No vision target found!')
            robot.drivetrain.move(0, 0, 0)


    def isFinished(self):
        return self._finished


    def end(self):
        print('GOTO TAPE ENDED\n\n\n\n\n')
        robot.drivetrain.move(0, 0, 0)

        self.nt.putNumber('pipeline', self.drivePipeID)
