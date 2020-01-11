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
        self.drive = NetworkTables.getTable('DriveTrain')

        self.tape = Config('limelight/tv', 5)
        self.strafe = Config('limelight/tx', 0)
        self.yDiff = Config('limelight/ty', 0)

        self.tapeoffset = Config('DriveTrain/tapeoffset', 0)

        self.pipeID = pipeID

        self.drivePipeID = 0 # Make this your basic drive pipeline.

        self.x = 0
        self.y = 0
        self.rotate = 0

        self.speedBoost = Config('DriveTrain/tapespeedboost', 1)



    def initialize(self):
        self.fY = self.drive.getValue('degreesfinished', 1)

        self.nt.putNumber('pipeline', self.pipeID)

        self._finished = False

        self.count = 0

    def execute(self):

        # h; High goal height -  limelight height (height difference)
        # y; Gets theta in degrees (29* is there as an already set, calculated value based off of config and setup (bumpers in front of initiation line (towards generator)
        #


        if self.tape.getValue() == 1:
            y = self.yDiff.getValue() + 29
            h = 68

            distance = h / math.tan(math.radians(y))

            print(str(distance))

            self._finished = False

        #print(self.tape.getValue())
        #if self.tape.getValue() == 1:
            #oX = self.strafe.getValue() - self.tapeoffset # 2.5
            #oY = self.distance.getValue()
            #theta = math.radians(oY+79.9)

            #oD = 2.5 * math.tan(theta)
            #oD = oD - 14
            ##oD = abs(oD)

            #if self.count < 4:
                #self.count += 1
            #else:
                #self.count = 0
                #self.nt.putNumber('snapshot', 1)

            #if abs(oX) > 10 :
                #self.rotate = math.copysign(.30,oX)
            #elif abs(oX) > 5 :
                #self.rotate = math.copysign(.25, oX)
            #elif abs(oX) > 3 :
                #self.rotate = math.copysign(.20, oX)
            #elif abs(oX) > 1 :
                #self.rotate = math.copysign(.15, oX)
            #else:
                #self.rotate = 0


            #self.y = oD * self.speedBoost * .01
            #if self.y < .175:
                #self.y = .175
            #if self.y > .35:
                #self.y = .35


            #robot.drivetrain.move(self.x, self.y, self.rotate)

            #print('oy = ' + str(oY) + " od = "+ str(oD))
            #if not self._finished:
                ##self._finished = oD <= 0.390
                #self._finished = oY <= self.fY


        #else:
            ##robot.lights.solidRed()
            #print('No vision target found!')
            #robot.drivetrain.move(0, 0, 0)


    def isFinished(self):
        return self._finished


    def end(self):
        print('GOTO TAPE ENDED\n\n\n\n\n')
        robot.drivetrain.move(0, 0, 0)

        self.nt.putNumber('pipeline', self.drivePipeID)
