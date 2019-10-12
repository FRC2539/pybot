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
            print("low camera, elev: "+ str(robot.elevator.getPosition()) + " arm: "+ str(robot.arm.getPosition()))
        else:
            print("standard camera")
            print("standard camera, elev: "+ str(robot.elevator.getPosition()) + " arm: "+ str(robot.arm.getPosition()))

        if self.originallyFieldOriented:
            robot.drivetrain.toggleFieldOrientation()

        #self.low = True

        if not self.low:
            self.nt.putNumber('pipeline', self.pipeID)
            self.ntLow.putNumber('pipeline', 0)
        else:
            self.ntLow.putNumber('pipeline', 1)


        self._finished = False

    def execute(self):
        slowdown=1
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


                h= 28.5 - 10.875

                theta = math.radians(63.9 + oY)

                oD = h * math.tan(theta) - 36

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
                    #if (oD > 36 ):
                        #self.y = .40
                    #elif (oD > 24):
                        #self.y = .30
                    #elif (oD > 12):
                        #self.y = .01

                self.y = (oD * oD) / self.speedBoost + .15


                if (self.y < .15) :
                    self.y = .15



                #oY2  = oY




                #self.x = math.copysign((oX * 4) / 100, oX)
                #self.y = math.copysign((oY2 * 6) / 100, oY)
                #self.rotate = self.x / frr

                #if abs(self.x) > 0.35:
                    #self.rotate = math.copysign(0.35, self.x)
                #elif abs(oX) <= 1.0:
                    #self.rotate = (oX / 10.0)/1.5
                #elif abs(oX) > 1.0 and abs(self.x) < 0.2:
                    #self.rotate = math.copysign(0.1, oX)/1.5


                #if self.y > 0.50:
                    #self.y = 0.50
                #elif oY <= 0.0:
                    #self.y = 0
                #elif oY > 0.0 and self.y < 0.3:
                    #self.y = 0.4

                #self.rotate = self.rotate * 2 # Was 0.5

                #'''
                #if oY <= 2.0:
                    #self.y = 0.1
                #'''
                ##slows  it down if it is closer than 3.5 degrees
                #if oY > 5 :
                    #self.y = .25
                #if oY <= 5:
                    #self.y = 0.15
                    #self.rotate = self.rotate * .75

                self.x = 0
                robot.drivetrain.move(self.x/slowdown, self.y/slowdown, self.rotate)



                if self.wantsHatch:
                    self._finished = robot.hatch.hasHatchPanel()

                elif not self._finished:
                    #self._finished = (abs(self.x) <= 0.03 and abs(self.y) <= 0.03 and abs(self.rotate) <= 0.03) or oY <= 1.0
                    self._finished = (abs(oX) - self.tapeoffset) <= 2.0 and oY <= 1.0
# if using the lower limelight/ arm is high
        elif self.low:
            if self.tapeLow.getValue() == 1:
                cald=4
                print(self.distanceLow.getValue())
                oX = self.strafeLow.getValue() + self.tapeoffset #0.0 #3.5 #Adjust for off center camera position
                oY = -1 * self.distanceLow.getValue()

                self.x = math.copysign((oX * (4/2)) / 100, oX)
                self.y = math.copysign((oY * (6/2)) / 100, oY)

                h= 39.5-28.4

                oD = h / math.tan((oY-15))

                self.y = .15

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
                    if (oD > 36 ):
                        self.y = .40
                    elif (oD > 24):
                        self.y = .20
                    elif (oD > 12):
                        self.y = .01


                if (self.y < .175) :
                    self.y = .175


                #start of working code
                #if (oY<-cald):
                    #oY2 = oY + cald
                #elif (oY>5):
                    #oY2 = oY - cald

                #self.rotate = self.x / frr

                #if abs(self.x) > 0.35:
                    #self.rotate = math.copysign(0.35, self.x)
                #elif abs(oX) <= 1.0:
                    #self.rotate = (oX / 10.0)/1.5
                #elif abs(oX) > 1.0 and abs(self.x) < 0.2:
                    #self.rotate = math.copysign(0.1, oX)/1.5

                #self.rotate = self.rotate * 2


                #if oY > 5 :
                    #self.y = .22
                #elif oY >3.5:
                    #self.y = .15
                #elif oY <=0:
                    #self.y = 0

                #self.y = self.y * self.speedBoost

                #if self.y < 0.15:
                    #self.y = 0.15

                #end of working code

                robot.drivetrain.move(self.x/slowdown, self.y/slowdown, self.rotate)


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

        if self.originallyFieldOriented:
            robot.drivetrain.toggleFieldOrientation()

        robot.lights.off()
