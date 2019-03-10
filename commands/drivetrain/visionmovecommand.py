from wpilib.command.command import Command

#from networktables import NetworkTables

from custom.config import Config

from commands.network.alertcommand import AlertCommand

import math

import socket
#import time

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

        self.stopDistance = 120
        #self.num = 0



        #UDP_IP = "10.25.39.2"
        #UDP_PORT = 5809

        #try:
        #    self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #    self.sock.bind((UDP_IP, UDP_PORT))
        #except:
        #    print("no udp")
        #    self.sock = -1

        self.maxSpeed = 50

        print("initialize visionmove")



    def execute(self):


        self.tapeFound = abs(Config('limelight/tv',False))
        print("tapefound- "+ str(self.tapeFound))
        self.tapeX = int(Config('limelight/tx',-1))
        self.tapeDistance = float(Config('limelight/ty',-1))
        speed = 0

        if self.tapeFound == True:
            self.reverse = False
            #print("has tape")
            #print("tapeX: "+str(self.tapeX))
            print("tapeDistance: " + str(self.tapeDistance))
            if self.tapeDistance <= 95 and self.tapeDistance > 55:
                print("slow down")
                speed = 25
                robot.drivetrain.move(0, 0, 0)
            elif self.tapeDistance <= int(self.stopDistance):
                print("under 60: "+str(self.tapeDistance))
                if self.demo == True and self.tapeDistance <= 45:
                    print("under 40: "+str(self.tapeDistance))
                    speed = 25
                    #self.tapeDistance -= 50
                    self.reverse = True
                elif self.demo == True:
                    print("demo mode and close, stop")
                    speed = 0
                    robot.drivetrain.move(0, 0, 0)
                    robot.drivetrain.movePer(0, 0)
                else:
                    print("not demo or between 40 and 60: "+str(self.tapeDistance))
                    #speed = 50
                    robot.drivetrain.move(0, 0, 0)
                    robot.drivetrain.movePer(0, 0)
                    self._finished = True
                #print("close, now stop")
                #robot.drivetrain.move(0, 0, 0)
            else:
                if self.demo == True:
                    speed = 50
                else:
                    #print("100 percent of max speed")
                    speed = 50

            if speed <= self.maxSpeed:
                tspeed = (speed / self.maxSpeed)/2
            else:
                tspeed = (self.maxSpeed / speed)

            print("setting speed: "+str(tspeed))

            lspeed = tspeed
            rspeed = tspeed

            #print("tapeX: "+str(self.tapeX))
            if self.tapeX <= -.5:
                #print("tape is left: "+str(self.tapeX))
                rspeed = tspeed - (.05 * self.tapeX)

            elif self.tapeX >= +.5:
                #print("tape is right: "+str(self.tapeX))
                rspeed = tspeed - (.05 * self.tapeX)

            if self.reverse == True:
                lspeed = lspeed * -1
                rspeed = rspeed * -1

            #print("r: "+str(rspeed)+" l:"+str(lspeed))
            robot.drivetrain.movePer(lspeed, rspeed)

        else:
            robot.drivetrain.move(0, 0, 0)
            robot.drivetrain.movePer(0, 0)
        #self.num = 0

            #self.num += 1


    def isFinished(self):
        #print("check finished: "+ str(self._finished))
        #if self.heading == robot.drivetrain.getPositions():
        #    self._finished = True
        #    print("finished")
        if self.demo == False and self.tapeDistance <= 55:
            robot.drivetrain.move(0, 0, 0)
            robot.drivetrain.movePer(0, 0)
            self.finished = True
            print("el fin")

        return self._finished


    def end(self):
        #robot.drivetrain.stop()

        print("ended visionmove")
