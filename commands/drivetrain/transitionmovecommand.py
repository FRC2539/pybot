from wpilib.command.command import Command

from custom.config import Config

import math

import robot

class TransitionMoveCommand(Command):

    def __init__(self,slowspeed,highspeed,transitionDistance,endDistance,rotateDistance=0,degrees=0):
        super().__init__('leave Ramp')

        #super().__init__(slowspeed, highspeed, transitionDistance, endDistance, rotateDistance, degrees)
        #super().__init__(degrees, False, name)

        self.requires(robot.drivetrain)


        self.slowspeed = slowspeed / 100
        self.highspeed = highspeed / 100
        self.transitionDistance = transitionDistance * Config('DriveTrain/ticksPerInch')
        self.endDistance = endDistance * Config('DriveTrain/ticksPerInch')

        self.rotateDistance = rotateDistance * Config('DriveTrain/ticksPerInch')
        self.degrees = degrees
        #self.startAngle = robot.drivetrain.getAngle()


        print("init")


    def initialize(self):
        #print("command slow: " +str(self.slowspeed)+ "high: " + str(self.highspeed))
        self.startPositions = robot.drivetrain.getPositions()
        self.startAngle = robot.drivetrain.getAngle()
        #print("initialize "+ str(self.slowspeed) + ", " + str(self.highspeed)+", "+str(self.transitionDistance)+", "+str(self.endDistance)+", "+str(self.rotateDistance)+", "+str(self.degrees))

        self.transited = False
        self.rotated = False
        self.rotating = False
        self._finished = False

        self.travelturndistance = 0

    def execute(self):
        #slowspeed,highspeed,transitionDistance,endDistance,rotateDistance=0,degrees=0
        #print("execute: " + str(self.slowspeed) + ", " + str(self.highspeed)+", "+str(self.transitionDistance)+", "+str(self.endDistance)+", "+str(self.rotateDistance)+", "+str(self.degrees))

        currentPositions = robot.drivetrain.getPositions()

        #print("totalTravel: "+str((self.startPositions[0] - currentPositions[0])/Config('DriveTrain/ticksPerInch')))
        #print("startPos: " + str(self.startPositions[0]) + " currentPos: " + str(currentPositions[0]))

        #print("move and monitor: "+ str(currentPositions))
        if self.transited:
            currentspeed = self.highspeed
        else:
            currentspeed = self.slowspeed



        #if abs(self.degrees > 0):
        #     self.distance =  abs(currentPositions[0]) - abs(self.startPositions[0])
        #else:
        #    self.distance =  abs(currentPositions[1]) - abs(self.startPositions[1])

        self.distance = abs(currentPositions[0] - currentPositions[1]) - abs(self.startPositions[0] - self.startPositions[1])
        if self.distance < 0:
            self.distance = self.distance *-1

        print("distance: "+ str(self.distance / Config('DriveTrain/ticksPerInch')) + " td: "+ str(self.transitionDistance / Config('DriveTrain/ticksPerInch')) + " ed: "+ str(self.endDistance / Config('DriveTrain/ticksPerInch')))
        if (abs(self.rotated) == True or abs(self.rotating) == True or (abs(self.distance) >= abs(self.transitionDistance) and abs(self.distance) <= abs(self.endDistance))) and self.transited == False:
            #if abs(self.rotated == True) or ((abs(self.rotating == False) and (abs(self.rotateDistance) > abs(self.distance)) or abs(self.rotateDistance) == 0)):
            #print("td: " + str(self.transitionDistance / Config('DriveTrain/ticksPerInch')) + " d: " + str(self.distance / Config('DriveTrain/ticksPerInch')) + " r: " + str(self.rotated / Config('DriveTrain/ticksPerInch')) + " rd: " + str(self.rotateDistance / Config('DriveTrain/ticksPerInch')))
            if (self.distance > self.transitionDistance and (abs(self.rotated) == True or abs(self.rotateDistance) == 0) or abs(self.rotateDistance) > self.transitionDistance):
                print("transition now")
                self.transited = True
                currentspeed = self.highspeed
                #currentspeed = 0
            elif abs(self.distance) >= abs(self.rotateDistance):
                self.rotating = True
                self.travelturndistance = self.distance
                print("finish rotating")
                #currentspeed = 0
        elif abs(self.distance) >= abs(self.endDistance):

            print("end now, d: "+ str(self.distance)+" ed: "+str(self.endDistance) + "ttd: " + str(self.travelturndistance))
            #currentspeed = 0
            self._finished = True

        print("currentspeed: "+str(currentspeed))
        rspeed = currentspeed
        lspeed = currentspeed

        #print("sd: "+ str(self.distance) + " rd: "+ str(self.rotateDistance))
        targetAngle = 0
        if abs(self.distance) >= abs(self.rotateDistance):
            #direction = ""
            #if self.degrees > 0:
            #    direction = "add"
            #else:
            #    direction = "subtract"

            targetAngle = self.startAngle + self.degrees
            if targetAngle > 360:
                targetAngle = targetAngle - 360


            currentAngle = robot.drivetrain.getAngle()

            angleDiff = self.angleDifference(currentAngle, targetAngle)
            #print("angleDiff: "+str(angleDiff))
            if (-1 <= angleDiff <= 1):
                #print("good and done rotating")
                self.rotating = False
                self.rotated = True
                if self.rotateDistance != 0 and abs(self.distance) >= abs(self.endDistance):
                    self._finished = True
                elif abs(self.distance) >= abs(self.endDistance):
                    #print("turning done and past end distance")
                    self._finished = True
            else:
                if self.rotating == True:
                    lspeed = currentspeed + (.005) * angleDiff
                    rspeed = currentspeed - (.005) * angleDiff
                else:
                    lspeed = currentspeed + (.005) * angleDiff

            '''
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
            if ((lowtarget) <= currentAngle <= (hightarget)):
                print("good and done rotating")
                self.rotating = False
                self.rotated = True
                if self.rotateDistance != 0 and abs(self.distance) >= abs(self.endDistance):
                    self._finished = True
                elif abs(self.distance) >= abs(self.endDistance):
                    self._finished = True
            else:
                if direction == "add":
                    print("go right")
                    #if abs(currentspeed) > 0:
                    #    rspeed = currentspeed - (.5) #* targetAngle
                    #else:
                    if self.rotating == True:
                        lspeed = currentspeed + (.5) #* targetAngle
                        rspeed = currentspeed - (.5) #* targetAngle
                    else:
                        lspeed = currentspeed + (.5) #* targetAngle
                else:
                    print("go left")
                    #if abs(currentspeed) > 0:
                    #    lspeed = currentspeed - (.5) #* targetAngle
                    #else:
                    if self.rotating == True:
                        rspeed = currentspeed + (.5) #* targetAngle
                        lspeed = currentspeed - (.5) #* targetAngle
                    else:
                        rspeed = currentspeed + (.5) #* targetAngle
            '''



        #print("speed: "+str(currentspeed))

        robot.drivetrain.movePer(lspeed, rspeed)

    def angleDifference(self, a1, a2):
        r = (a2 -a1) % 360
        if (r < -180):
            r += 360
        if (r >= 180):
            r -= 360
        return r

    def isFinished(self):

        if abs(self.distance) >= abs(self.endDistance):
            print("finished")
            robot.drivetrain.move(0, 0, 0)
            robot.drivetrain.movePer(0, 0)
            self._finished = True
        return self._finished


    def end(self):
        #robot.drivetrain.stop()

        print("end")
        print(str(self.distance) + "   " + str(self.endDistance))
        print('TPI: ' + str(abs(Config('DriveTrain/ticksPerInch'))))
