from wpilib.command.command import Command

from custom.config import Config

import math

import robot

class leaveRampCommand(Command):

    def __init__(self,slowspeed,highspeed,transitionDistance,endDistance,rotateDistance=0,degrees=0):
        #super().__init__('leave Ramp')

        super().__init__('leave Ramp')

        self.requires(robot.drivetrain)

        self._finished = False
        self.slowspeed = slowspeed / 100
        self.highspeed = highspeed / 100
        self.transitionDistance = transitionDistance * Config('DriveTrain/ticksPerInch')
        self.endDistance = endDistance * Config('DriveTrain/ticksPerInch')

        #print("ss: "+str(self.slowspeed))
        #print("hs: "+str(self.highspeed))
        #print("ts: "+str(self.transitionDistance))
        #print("ed: "+str(self.endDistance))
        robot.drivetrain.resetGyro()
        self.rotateDistance = rotateDistance * Config('DriveTrain/ticksPerInch')
        self.degrees = degrees
        self.startAngle = robot.drivetrain.getAngle()
        #self.targetDegrees = robot.drivetrain.getAngleTo(degrees)

        #if self.targetDegrees < 0:
        #    self.targetDegrees = 360 + self.targetDegrees

        #self.targetAngle = self.startAngle + self.degrees

        #self.transitionDistance = self.transitionDistance + self.startPositions[0]

        #print("startAngle: "+ str(self.startAngle))

    def initialize(self):
        self.startPositions = robot.drivetrain.getPositions()
        self.startAngle = robot.drivetrain.getAngle()

    def execute(self):
        currentPositions = robot.drivetrain.getPositions()

        print("startPos: " + str(self.startPositions[0]) + " currentPos: " + str(currentPositions[0]))

        #print("move and monitor: "+ str(currentPositions))
        currentspeed = self.slowspeed



        self.distance =  currentPositions[0] - self.startPositions[0]
        print("distance: "+ str(self.distance) + " td: "+ str(self.transitionDistance))
        if  self.distance >= self.transitionDistance and self.distance <= self.endDistance:
            print("transition now")
            currentspeed = self.highspeed
            #currentspeed = 0
        elif self.distance >= self.endDistance:

            print("end now: "+ str(self.endDistance))
            currentspeed = 0

        rspeed = currentspeed
        lspeed = currentspeed

        #print("sd: "+ str(self.distance) + " rd: "+ str(self.rotateDistance))

        if self.distance >= self.rotateDistance:
            #print("past rotateDistance: " + str(self.rotateDistance))
            #print("degrees: " + str(self.degrees) + " angle progress: " + str(robot.drivetrain.getAngle() - self.startAngle))

            #if self.targetDegrees < 0:
            #    self.directionX = (self.startAngle - robot.drivetrain.getAngle()) - self.degrees
            #else:
            #    self.directionX = self.degrees - (robot.drivetrain.getAngle() - self.startAngle)
            #print("directionX: "+str(self.directionX))
            direction = ""
            if self.degrees > 0:
                direction = "add"
            else:
                direction = "subtract"

            targetAngle = self.startAngle + self.degrees
            if targetAngle > 360:
                targetAngle = targetAngle - 360


            currentAngle = robot.drivetrain.getAngle()


            lowtarget = targetAngle - 5
            if lowtarget < 0:
                if direction == "subtract":
                    lowtarget = 360 + lowtarget
                else:
                    lowtarget = 360 - lowtarget

            hightarget = targetAngle + 5
            if hightarget > 360:
                if direction == "subtract":
                    hightarget = 360 + hightarget
                else:
                    hightarget = hightarget - 360

            print("startAngle: " + str(self.startAngle) + "currentAngle: " +str(currentAngle) + " targetAngle: " + str(targetAngle) + " ht: " + str(hightarget) + " lt: " + str(lowtarget)  )

            if (lowtarget) <= currentAngle <= (hightarget):
                print("good")
                self._finished = True
            else:
                if direction == "add":
                    print("go right")
                    rspeed = currentspeed - (.5) #* self.targetDegrees
                else:
                    print("go left")
                    lspeed = currentspeed - (.5) #* self.targetDegrees




        print("speed: "+str(currentspeed))

        robot.drivetrain.movePer(lspeed, rspeed)

    def _calculateDisplacement(self):
        '''
        In order to avoid having a separate ticksPerDegree, we calculate it
        based on the width of the robot base.
        '''
        inchesPerDegree = math.pi * Config('DriveTrain/width') / 360
        totalDistance = self.degrees * inchesPerDegree

        return totalDistance * 2

    def isFinished(self):

        #if self.distance >= self.endDistance:
        #    self._finished = True
        return self._finished


    def end(self):
        #robot.drivetrain.stop()

        print("end")
