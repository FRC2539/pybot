from wpilib.command.command import Command


from networktables import NetworkTables

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
        self.transitionDistance = transitionDistance

        self.endDistance = endDistance

        self.rotateDistance = rotateDistance
        self.degrees = degrees
        #self.startAngle = robot.drivetrain.getAngle()


        print("init")


    def initialize(self):





        #self.transitionDistance = self.transitionDistance * self.tpi
        #self.endDistance = self.endDistance * self.tpi
        #self.rotateDistance = self.rotateDistance * self.tpi

        #print("raw endDistance: "+ str(self.endDistance)+" tpi: " + str(self.tpi))

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

        self.tpi = Config('DriveTrain/ticksPerInch', 0)

        transitionDistance = self.transitionDistance * self.tpi
        endDistance = self.endDistance * self.tpi
        rotateDistance = self.rotateDistance * self.tpi

        currentPositions = robot.drivetrain.getPositions()
        print("c0: "+str(currentPositions[0]) + "c1: "+str(currentPositions[1]))

        if self.transited:
            currentspeed = self.highspeed
        else:
            currentspeed = self.slowspeed

        currentPos = abs(currentPositions[0]) # - currentPositions[1])
        startPos = abs(self.startPositions[0]) # - self.startPositions[1])

        if currentPos < 0:
            currentPos = currentPos *-1

        if startPos < 0:
            startPos = self.distance *-1

        self.distance = currentPos - startPos
        if self.distance < 0:
            self.distance = self.distance *-1

        print("tpi: "+ str(self.tpi))
        print("distance: "+ str(self.distance / self.tpi) + " td: "+ str(transitionDistance / self.tpi) + " ed: "+ str(endDistance / self.tpi) + " rd: "+ str(rotateDistance / self.tpi) + " d: "+ str(self.degrees))
        #print("raw distance: "+ str(self.distance) + " td: "+ str(transitionDistance) + " ed: "+ str(endDistance))
        if (abs(self.rotated) == True or abs(self.rotating) == True or (abs(self.distance) >= abs(transitionDistance) and abs(self.distance) <= abs(endDistance))) and self.transited == False:
            #if abs(self.rotated == True) or ((abs(self.rotating == False) and (abs(self.rotateDistance) > abs(self.distance)) or abs(self.rotateDistance) == 0)):
            #print("td: " + str(transitionDistance / self.tpi) + " d: " + str(self.distance / self.tpi) + " r: " + str(self.rotated / self.tpi) + " rd: " + str(self.rotateDistance / self.tpi))
            if (self.distance > transitionDistance and (abs(self.rotated) == True or abs(rotateDistance) == 0) or abs(rotateDistance) > transitionDistance):
                print("transition now")
                self.transited = True
                currentspeed = self.highspeed
                #currentspeed = 0
            elif abs(self.distance) >= abs(rotateDistance):
                self.rotating = True
                self.travelturndistance = self.distance
                print("finish rotating")
                #currentspeed = 0
        elif abs(self.distance) >= abs(endDistance):

            print("end now, d: "+ str(self.distance)+" ed: "+str(endDistance) + "ttd: " + str(self.travelturndistance))
            #currentspeed = 0
            self._finished = True

        #print("currentspeed: "+str(currentspeed))
        rspeed = currentspeed
        lspeed = currentspeed

        #print("sd: "+ str(self.distance) + " rd: "+ str(self.rotateDistance))
        targetAngle = 0
        if abs(self.distance) >= abs(rotateDistance):

            targetAngle = self.startAngle + self.degrees
            if targetAngle > 360:
                targetAngle = targetAngle - 360


            currentAngle = robot.drivetrain.getAngle()

            angleDiff = self.angleDifference(currentAngle, targetAngle)
            print("rotate now, ad: "+ str(angleDiff))
            if (-2 <= angleDiff <= 2):
                print("good and done rotating")
                self.rotating = False
                self.rotated = True
                if rotateDistance != 0 and abs(self.distance) >= abs(endDistance):
                    self._finished = True
                elif abs(self.distance) >= abs(endDistance):
                    print("turning done and past end distance")
                    self._finished = True
            else:
                if self.rotating == True:
                    lspeed = currentspeed + (.005) * (angleDiff/.25)
                    rspeed = currentspeed - (.005) * (angleDiff/.25)
                else:
                    lspeed = currentspeed + (.005) * (angleDiff/.25)

        robot.drivetrain.movePer(lspeed, rspeed)

    def angleDifference(self, a1, a2):
        r = (a2 -a1) % 360
        if (r < -180):
            r += 360
        if (r >= 180):
            r -= 360
        return r

    def isFinished(self):
        distance = self.distance #* Config('DriveTrain/ticksPerInch', 0)
        endDistance = self.endDistance * Config('DriveTrain/ticksPerInch', 0)
        if distance < 0:
            distance = distance * -1

        if endDistance < 0:
            endDistance = endDistance * -1

        if abs(distance) >= abs(endDistance):
            print("finished")
            robot.drivetrain.move(0, 0, 0)
            robot.drivetrain.movePer(0, 0)
            self._finished = True
        return self._finished


    def end(self):
        #robot.drivetrain.stop()

        print("end")
        #print(str(self.distance) + "   " + str(self.endDistance))
        #print('TPI: ' + str(abs(self.tpi)))
