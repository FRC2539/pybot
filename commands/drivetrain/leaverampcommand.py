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

        self.rotateDistance = rotateDistance * Config('DriveTrain/ticksPerInch')
        self.degrees = degrees
        self.startAngle = robot.drivetrain.getAngle()


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

    def angleDifference(self, a1, a2):
        r = (a2 -a1) % 360
        if (r < -180):
            r += 360
        if (r >= 180):
            r -= 360
        return r

    def isFinished(self):

        if self.distance >= self.endDistance:
            print("finished")
            robot.drivetrain.move(0, 0, 0)
            robot.drivetrain.movePer(0, 0)
            self._finished = True
        return self._finished


    def end(self):
        #robot.drivetrain.stop()

        print("end")
