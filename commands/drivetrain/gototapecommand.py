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
                #ox=origninal x in degrees from tape and xy= original y from tape
                oX = self.strafe.getValue() + self.tapeoffset #0.0 #3.5 #Adjust for off center camera position
                oY = self.distance.getValue()
                #totalspeed = 0
                #totalmotors = 0

                #speed = robot.drivetrain.getSpeeds()
                #for speeds in speed:
                    #totalspeed += speeds
                    #totalmotors += 1
                #avgspeed = totalspeed/totalmotors
                #totv = 0
                #numm = 0
                #for motors in self.motors:
                    #totv += self.motors.getVelocity()
                    #print ('Velocity: ' + self.motors.getVelocity())
                    #numm += 1

                #avgv = totv / numm
                #print ('Avg Velocity: '+ avgv)
                oY2  = oY

                #trying to set up the consistency
                if (oY<-5):
                    oY2 = oY + 5
                elif (oY>5):
                    oY2 = oY - 5


                self.x = math.copysign((oX * 4) / 100, oX)
                self.y = math.copysign((oY2 * 6) / 100, oY)
                self.rotate = self.x / frr

                #if the speed is greater than 35% then set it to 35% keeping the direction
                if abs(self.x) > 0.35:
                    self.x = math.copysign(0.35, self.x)
                    self.rotate = self.x / frr
                #if the target in degrees is less than or equal to 1 then make the speed equal to the degrees over 10
                #also stop turning as much
                elif abs(oX) <= 1.0:
                    self.x = oX / 10.0
                    self.rotate = self.x / crr
                #if the target in degrees is greater than 1, and the speed is lower than 20% then set:
                #the the x speed to the same directionas the target x and the 20% speed
                #make the get the rotate from the x speed
                elif abs(oX) > 1.0 and abs(self.x) < 0.2:
                    self.x = math.copysign(0.2, oX)
                    self.rotate = math.copysign(0.1, oX) / crr

                if self.y > 0.50:
                    self.y = 0.50
                elif oY <= 0.0:
                    self.y = 0
                elif oY > 0.0 and self.y < 0.3:
                    self.y = 0.4

                if oY <= 10.0: # Was 4.0
                    self.rotate = self.rotate * 2 # Was 0.5
                '''
                if oY <= 2.0:
                    self.y = 0.1
                '''
                #slows  it down if it is closer than 3.5 degrees
                if oY <= 5:
                    #if avgspeed > 5:
                        #self.stop()
                    self.y = 0.15
                self.y = self.y * self.speedBoost
                if self.y < 0.15:
                    self.y = 0.15


                robot.drivetrain.move(self.x/slowdown, self.y/slowdown, self.rotate)



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

                self.x = math.copysign((oX * (4/2)) / 100, oX)
                self.y = math.copysign((oY * (6/2)) / 100, oY)

                if (oY<-5):
                    oY2 = oY + 5
                elif (oY>5):
                    oY2 = oY - 5

                self.rotate = self.x / frr

                if abs(self.x) > 0.35:
                    self.x = math.copysign(0.45, self.x)
                    self.rotate = self.x / frr
                elif abs(oX) <= 1.0:
                    self.x = oX / 10.0
                    self.rotate = self.x / crr
                elif abs(oX) > 1.0 and abs(self.x) < 0.2:
                    self.x = math.copysign(0.2, oX)
                    self.rotate = math.copysign(0.3, oX) / crr


                if oY <= 8.0:
                    self.rotate = 0.0


                if oY > 5 :
                    self.y = .22
                elif oY >3.5:
                    self.y = .15
                elif oY <=0:
                    self.y = 0

                self.y = self.y * self.speedBoost

                if self.y < 0.15:
                    self.y = 0.15

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
