from wpilib.command.command import Command

from custom.config import Config

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

        print("ss: "+str(self.slowspeed))
        print("hs: "+str(self.highspeed))
        print("ts: "+str(self.transitionDistance))
        print("ed: "+str(self.endDistance))

        self.rotateDistance = rotateDistance * Config('DriveTrain/ticksPerInch')
        self.degrees = degrees

        self.startPositions = robot.drivetrain.getPositions()
        self.startAngle = robot.drivetrain.getAngle()
        #self.targetAngle = self.startAngle + self.degrees

        print("startAngle: "+ str(self.startAngle))


    def execute(self):
        currentPositions = robot.drivetrain.getPositions()
        print("move and monitor: "+ str(currentPositions))
        currentspeed = self.slowspeed
        self.distance = self.startPositions[1] - currentPositions[1]
        print("distance: "+ str(self.distance))
        if  self.distance >= self.transitionDistance and self.distance <= self.endDistance:
            print("transition now")
            currentspeed = self.highspeed
        elif self.distance >= self.endDistance:
            print("end now")
            currentspeed = 0

        rspeed = currentspeed
        lspeed = currentspeed

        print("sd: "+ str(self.distance) + " rd: "+ str(self.rotateDistance))

        if self.distance >= self.rotateDistance:

            self.tapeX = self.degrees - (robot.drivetrain.getAngle() - self.startAngle)
            print("tapeX: "+str(self.tapeX))

            if self.tapeX <= -.5:
                print("direction is left: "+str(self.tapeX))
                rspeed = currentspeed - (.5) #* self.tapeX

            elif self.tapeX >= +.5:
                print("direction is right: "+str(self.tapeX))
                rspeed = currentspeed - (.5) #* self.tapeX


        robot.drivetrain.movePer(lspeed, rspeed)

    def isFinished(self):

        if self.distance >= self.endDistance:
            self._finished = True
        return self._finished


    def end(self):
        #robot.drivetrain.stop()

        print("end")
