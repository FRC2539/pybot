from wpilib.command.command import Command
from custom.config import Config
import math
import robot

from networktables import NetworkTables

class GoToTapeCommand(Command):

    def __init__(self, pipeID=1):
        super().__init__('Go To Tape')

        self.requires(robot.drivetrain)

        self.tape = Config('limelight/tv', 0)
        self.strafe = Config('limelight/tx', 0)
        self.distance = Config('limelight/ty', 0)

        self.tapeLow = Config('limelight-low/tv', 0)
        self.strafeLow = Config('limelight-low/tx', 0)
        self.distanceLow = Config('limelight-low/ty', 0)

        self.tapeoffset = Config('DriveTrain/tapeoffset', 0)

        self.nt = NetworkTables.getTable('limelight')
        self.ntLow = NetworkTables.getTable('limelight-low')

        self.pipeID = pipeID

        self.drivePipeID = 0 # Make this your basic drive pipeline.

        self.x = 0
        self.y = 0
        self.rotate = 0

        self.speedBoost = Config('DriveTrain/tapespeedboost', 1)


        self.originallyFieldOriented = True


    def initialize(self):
        self.originallyFieldOriented = robot.drivetrain.isFieldOriented
        self.wantsHatch = not robot.hatch.hasHatchPanel()

        self.low = False

        if (not self.wantsHatch) and robot.elevator.getPosition() >= 10.0:
            #if (not self.wantsHatch) and robot.elevator.getPosition() >= 25.0:
            #if robot.elevator.getPosition() >= 25.0:

            self.low = True
            #print("low camera, elev: "+ str(robot.elevator.getPosition()) + " arm: "+ str(robot.arm.getPosition()))
        else:
            #print("standard camera")
            pass
            #print("standard camera, elev: "+ str(robot.elevator.getPosition()) + " arm: "+ str(robot.arm.getPosition()))

        #self.low = True

        if not self.low:
            self.nt.putNumber('pipeline', self.pipeID)
            self.ntLow.putNumber('pipeline', 0)
            self.nt.putBoolean('snapshot', True)
        else:
            self.ntLow.putNumber('pipeline', 1)
            self.ntLow.putBoolean('snapshot', True)



        self._finished = False

    def execute(self):
        #closer rotate ratio
        crr=2.0
        #further rotate ratio
        frr=3.0
#if you are using the normal limelight
        if not self.low:

            if self.tape.getValue() == 1:
                print(self.distance.getValue())
                oX = self.strafe.getValue() + self.tapeoffset #0.0 #3.5 #Adjust for off center camera position
                oY = self.distance.getValue()


                h = 39.5 - 28.5

                theta = math.radians(73 + oY)

                oD = h * math.tan(theta) - 36

                if (abs(oX) > 10):
                    self.rotate = math.copysign(.20, oX)
                elif (abs(oX) >7):
                    self.rotate = math.copysign(.15, oX)
                elif (abs(oX) >5):
                    self.rotate = math.copysign(.10, oX)
                elif (abs(oX) >1):
                    self.rotate = math.copysign(.05, oX)
                else:
                    self.rotate = 0

                self.y = oD * .02
                self.y = self.y*self.speedBoost

                if (self.y < .15) :
                    self.y = .15

                if (self.y > .25):
                    self.y = .25

                self.x = 0

                print("oD= "+str(oD))

                robot.drivetrain.move(self.x, self.y, self.rotate)



                if self.wantsHatch:
                    self._finished = robot.hatch.hasHatchPanel()

                elif not self._finished:
                    #self._finished = (abs(self.x) <= 0.03 and abs(self.y) <= 0.03 and abs(self.rotate) <= 0.03) or oY <= 1.0
                    self._finished = (abs(oX) - self.tapeoffset) <= 2.0 and oY <= 1.0
# if using the lower limelight/ arm is high
        elif self.low:
            if self.tapeLow.getValue() == 1:
                print(self.distanceLow.getValue())
                oX = self.strafeLow.getValue() + self.tapeoffset #0.0 #3.5 #Adjust for off center camera position
                oY = -1 * self.distanceLow.getValue()

                #self.ntLow.putBoolean('snapshot', True)

                self.x = math.copysign((oX * (4/2)) / 100, oX)
                self.y = math.copysign((oY * (6/2)) / 100, oY)

                h = 28.5 - 10.875

                oD = (h / math.tan(math.radians(oY+36.3)) ) - 25

                self.y = .02 * oD

                if (abs(oX) > 10):
                    self.rotate = math.copysign(.25, oX)
                elif (abs(oX) >5):
                    self.rotate = math.copysign(.20, oX)
                elif (abs(oX) >3):
                    self.rotate = math.copysign(.15, oX)
                elif (abs(oX) >1):
                    self.rotate = math.copysign(.10, oX)
                else:
                    self.rotate = 0


                if (self.y < .175) :
                    self.y = .175
                print("oD= "+str(oD))
                self.y = self.y*self.speedBoost

                robot.drivetrain.move(self.x, self.y, self.rotate)

                if not self._finished:
                    self._finished = (abs(oX) - self.tapeoffset) <= 2.0 and oY <= 2.0

            if self._finished:
                robot.lights.solidGreen()
            else:
                robot.lights.solidBlue()

        else:
            robot.lights.solidRed()
            print('No vision target found!')
            robot.drivetrain.move(0, 0, 0)


    def isFinished(self):
        return self._finished


    def end(self):
        robot.drivetrain.move(0, 0, 0)

        self.nt.putNumber('pipeline', self.drivePipeID)
        self.ntLow.putNumber('pipeline', 0)
        if not self.low:
            self.nt.putBoolean('snapshot', True)
        else:
            self.ntLow.putBoolean('snapshot', True)

        robot.lights.off()
