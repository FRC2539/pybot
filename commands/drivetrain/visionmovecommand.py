from wpilib.command.command import Command

from custom.config import Config

from commands.network.alertcommand import AlertCommand

import math

import robot


class VisionMoveCommand(Command):

    def __init__(self, demo = False):
        super().__init__('visionmove')

        self.requires(robot.drivetrain)
        self.demo = demo


    def initialize(self):

        print("init vision move")

        self._finished = False

        self.degrees = -360
        self.tapeDistance = 0
        self.tapeFound = False

        self.stopDistance = 1


        self.maxSpeed = 20

        print("initialize visionmove")



    def execute(self):


        self.tapeFound = Config('limelight/tv',0)
        self.tapeX = Config('limelight/tx',0)
        self.tapeDistance = Config('limelight/ty',0)

        speed = 0

        if self.tapeFound == 1:
            self.reverse = False
            #print("has tape")
            #print("tapeX: "+str(self.tapeX))
            print("tapeDistance: " + str(self.tapeDistance))
            if self.tapeDistance <= 4 and self.tapeDistance > 1:
                print("slow down")
                speed = 5
                #robot.drivetrain.move(0, 0, 0)
            elif self.tapeDistance <= int(self.stopDistance):
                if self.demo == True and self.tapeDistance <= 2:
                    print("demo and close: "+str(self.tapeDistance))
                    speed = 20
                    #self.tapeDistance -= 50
                    self.reverse = True
                elif self.demo == True:
                    print("demo mode and close, stop")
                    speed = 0
                    #robot.drivetrain.move(0, 0, 0)
                    robot.drivetrain.movePer(0, 0)
                else:
                    print("not demo and in stop zone: "+str(self.tapeDistance))
                    speed = 0
                    #robot.drivetrain.move(0, 0, 0)
                    robot.drivetrain.movePer(0, 0)
                    self._finished = True
                #print("close, now stop")
                #robot.drivetrain.move(0, 0, 0)
            else:
                if self.demo == True:
                    speed = 20
                else:
                    #print("100 percent of max speed")
                    speed = 20

            if speed <= self.maxSpeed:
                tspeed = (speed / self.maxSpeed)/6
            else:
                tspeed = (self.maxSpeed / speed)/4

            #tspeed = 0

            print("setting speed: "+str(tspeed))

            print("tapeX degrees: "+str(self.tapeX))

            if self.tapeX > 12 or self.tapeX < -12:

                self.tapeX = self.tapeX /3
                print("over 12: "+str(self.tapeX))
            elif self.tapeX > 1 or self.tapeX < -1:
                print("under 5 but over 1")
                if self.tapeX < 0:
                    self.tapeX = -6.2
                else:
                    self.tapeX = 6.2

            lspeed = tspeed + (.04 * self.tapeX)
            rspeed = tspeed + (.04 * (self.tapeX)*-1)


            if self.reverse == True:
                lspeed = lspeed * -1
                rspeed = rspeed * -1

            print("r: "+str(rspeed)+" l:"+str(lspeed))
            robot.drivetrain.movePer(lspeed, rspeed)

        else:
            print("no tape")
            robot.drivetrain.move(0, 0, 0)
            robot.drivetrain.movePer(0, 0)



    def isFinished(self):
        #print("check finished: "+ str(self._finished))
        #if self.heading == robot.drivetrain.getPositions():
        #    self._finished = True
        #    print("finished")
        if self.demo == False and self.tapeDistance <= 2:
            #robot.drivetrain.move(0, 0, 0)
            #robot.drivetrain.movePer(0, 0)
            self.finished = True
            print("el fin")

        return self._finished


    def end(self):
        #robot.drivetrain.stop()

        print("ended visionmove")
