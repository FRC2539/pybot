from wpilib.command.command import Command

from networktables import NetworkTables

from custom.config import Config

from commands.network.alertcommand import AlertCommand

import math

import socket
#import time

import robot

class StateMachineTempCommand(Command):



    def __init__(self):
        super().__init__('State Machine Temp')
        print("init")

        self.requires(robot.drivetrain)

    def initialize(self):

        self._finished = False

        self.degrees = -360
        self.distance = self.degrees


        #self.num = 0



        UDP_IP = "10.25.39.2"
        UDP_PORT = 5809

        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.bind((UDP_IP, UDP_PORT))
        except:
            print("no udp")
            self.sock = -1

        self.maxSpeed = 50



    def execute(self):
        #if self.num >= 1:
            #robot.drivetrain.setPositions(self.targetPositions)

        if self.sock != -1:
            data, addr = self.sock.recvfrom(1024) # buffer size is 1024 bytes
            #print("1 received message:" + str(data))
            self.tmessage = data.decode("utf-8")
            self.message = self.tmessage.split(",")
            self.tapeFound = self.message[0].split(":")[1]
            self.tapeX = float(self.message[1].split(":")[1])
            self.tapeDistance = float(self.message[2].split(":")[1])

            if self.tapeFound == "True":
                #print("has tape")
                #print("tapeX: "+str(self.tapeX))
                #print("tapeDistance: " + str(self.tapeDistance))
                if self.tapeDistance <= 90 and self.tapeDistance > 55:
                    #print("slow down")
                    speed = 25
                    robot.drivetrain.move(0, 0, 0)
                elif self.tapeDistance <= 55:
                    speed = 0
                    #print("close, now stop")
                    robot.drivetrain.move(0, 0, 0)
                else:
                    #print("100 percent of max speed")
                    speed = 100

                if speed <= self.maxSpeed:
                    tspeed = (speed / self.maxSpeed)/2
                else:
                    tspeed = (self.maxSpeed / speed)

                #print("setting speed: "+str(tspeed))

                lspeed = tspeed
                rspeed = tspeed

                #print("tapeX: "+str(self.tapeX))
                if self.tapeX <= -.5:
                    #print("tape is left: "+str(self.tapeX))
                    rspeed = tspeed - (.05 * self.tapeX)

                elif self.tapeX >= +.5:
                    #print("tape is right: "+str(self.tapeX))
                    rspeed = tspeed - (.05 * self.tapeX)

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
        return self._finished


    def end(self):
        #robot.drivetrain.stop()

        print("end")
