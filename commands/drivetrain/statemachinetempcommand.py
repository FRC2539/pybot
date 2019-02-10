from wpilib.command.command import Command
#from magicbot import StateMachine
#from magicbot.magicrobot import MagicRobot
#from magicbot.state_machine import AutonomousStateMachine

#from magicbot.state_machine import state

#from commands.drivetrain.pivotcommand import PivotCommand

#from commands.drivetrain.pivotcommand import PivotCommand

#from movecommand import MoveCommand
from commands.drivetrain.pivotcommand import PivotCommand

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




        print("init-"+str(robot.drivetrain.getPositions()))
        self._finished = False

        self.degrees = -360
        self.distance = self.degrees
        reverse = False

        self.num = 0
        self.speedLimit = 800

        self.moving = False
        self.direction = 1

        # 0 = Left Side, 1 = Right Side
        self.pivotSide = 0
        if self.degrees < 0:
            self.pivotSide = 1

        if reverse:
            self.pivotSide = abs(self.pivotSide - 1)

        #print("exec")

        UDP_IP = "10.25.39.2"
        UDP_PORT = 5809

        try:

            #print("before udp")
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.bind((UDP_IP, UDP_PORT))

            #while True:
            #    data, addr = self.sock.recvfrom(1024) # buffer size is 1024 bytes
            #    print("1 received message:" + str(data))
            #print("after udp")



        except:
            print("no udp")
            self.sock = -1

        self.sign = 1

        #robot.drivetrain.setSpeedLimit(600)

        self.heading = []

        self._checkforTape()

        #robot.drivetrain.setPositions(self.targetPositions)




    def execute(self):
        #print("here")


        if self.num >= 20:
            #robot.drivetrain.setPositions(self.targetPositions)

            if self.sock != -1:
                data, addr = self.sock.recvfrom(1024) # buffer size is 1024 bytes
                #print("1 received message:" + str(data))
                self.tmessage = data.decode("utf-8")
                self.message = self.tmessage.split(",")
                self.tapeFound = self.message[0].split(":")[1]
                self.tapeX = float(self.message[1].split(":")[1])
                self.tapeDistance = float(self.message[2].split(":")[1])
                #self.tapeDistance -= 12
                print("ctd: "+str(self.tapeDistance) + " tx " + str(self.tapeX) + " tf"+ str(self.tapeFound))

                if self.tapeFound == "True":
                    print("has tape")
                    print("tapeX: "+str(self.tapeX))
                    self.tapeX = self.tapeX /4
                    print("tapeX_half: "+str(self.tapeX))
                    if self.tapeX <= -2 or self.tapeX >= 2:


                        offset = self._calculateDisplacement(self.tapeX) * self.direction
                        targetPositions = []
                        sign = 1

                        for i, position in enumerate(self.heading):
                            side = i % 2

                            if self.pivotSide == side:
                                position += offset
                                position = position * sign
                                sign *= -1

                            targetPositions.append(position)

                        if self.tapeDistance <= 70:
                            print("slow down")
                            robot.drivetrain.setSpeedLimit(200)

                        if self.tapeDistance <= 50:
                            #robot.drivetrain.move(0, 0, 0)
                            print("stop")
                            #robot.drivetrain.setPositions(robot.drivetrain.getPositions())
                            #robot.drivetrain.stop()

                        print("correcting turn"+ str(targetPositions))
                        robot.drivetrain.setPositions(targetPositions)


                #else:
                     #self._pivotandmove(0, 0)
                     #robot.drivetrain.move(0, 0, 0)

        #self._checkforTape()
            self.num = 0

        self.num += 1









    def _checkforTape(self):
        if self.sock != -1:
            data, addr = self.sock.recvfrom(1024) # buffer size is 1024 bytes
            #print("1 received message:" + str(data))
            self.tmessage = data.decode("utf-8")
            self.message = self.tmessage.split(",")
            self.tapeFound = self.message[0].split(":")[1]
            self.tapeX = float(self.message[1].split(":")[1])
            self.tapeDistance = float(self.message[2].split(":")[1])
            self.tapeDistance -= 12



            if self.tapeFound == "True":
                #print("tape")
                #self.offset = self.tapeX #(self.tapeX - (640/2))/640 * 5
                #print("offset: "+str(offset))
                #if tapeDistance <= 4:
                #    offset = 0
                #elif offset <= 5 and offset >= -5:
                #    offset = 0

                #if self.tapeX <= -1 or self.tapeX >= 1:

                    #print("tapeX within range: "+str(self.tapeX))
                    #self.tapeX = 0

                if self.tapeX <= 5 or self.tapeX >= -5:
                    print("rotate only over 5")
                    self.distance = 0

                robot.drivetrain.setSpeedLimit(800)
                if self.tapeDistance <= 40:
                    print("within 40")
                    #robot.drivetrain.move(0, 0, 0)
                    robot.drivetrain.setSpeedLimit(100)
                    #self.moveDistance = (self.tapeDistance)
                    #self.tapeDistance -= 70
                    #self.moveDistance = 0
                    #self.offset = 0
                    #print("too close, stopping")
                    #robot.drivetrain.stop()
                    #if self.tapeDistance <= 10:
                    #    self.moveDistance = (0)

                #else:
                    #robot.drivetrain.setSpeedLimit(800)
                    #self.offset = 0
                    #moveDistance = (tapeDistance - 60) * Config('DriveTrain/ticksPerInch')
                    #self.moveDistance = (self.tapeDistance)
                    #print("pivot and move: "+str(offset)+"% "+str(moveDistance))


                print("tf-"+str(self.tapeFound))
                print("tx: "+str(self.tapeX))
                print("td: "+str(self.tapeDistance))

                if self.tapeX == 0 and self.tapeDistance == 0:
                    print('no td and tx')
                else:
                    self._pivotandmove(self.tapeX, self.tapeDistance)



            else:
                print("no tape")
                #robot.drivetrain.stop()
                #robot.drivetrain.move(0, 0, 0)

    def _move(self, distance):
        self.targetPositions = []

        md = distance * Config('DriveTrain/ticksPerInch')#moveDistance
        self.x = 0
        for position in robot.drivetrain.getPositions():
            if self.x == 0 or self.x == 2:
                self.targetPositions.append(position + md)
            else:
                self.targetPositions.append(position - md)
            self.x += 1

        print("otarget-"+str(robot.drivetrain.getPositions()))
        print("ntarget-"+str(self.targetPositions))

        robot.drivetrain.setPositions(self.targetPositions)

    def _pivotandmove(self, tdegrees, tdistance):

        print("pm turning: "+ str(tdegrees))
        offset = self._calculateDisplacement(tdegrees) * self.direction
        #offset = 0
        tdistance = tdistance * Config('DriveTrain/ticksPerInch')
        #print("offset ticks: "+str(offset))
        #print("pm dist ticks: "+str(tdistance))
        targetPositions = []
        sign = 1

        for i, position in enumerate(robot.drivetrain.getPositions()):
            side = i % 2
            #print("side: "+str(self.pivotSide)+ " startPos: "+ str(position))
            if self.pivotSide == side:
                position += offset
                position = position * sign
                sign *= -1


            if i % 2 == 0:
                position += tdistance
            else:
                position -= tdistance

            #print("side: "+str(self.pivotSide)+ " setPos: "+ str(position))
            targetPositions.append(position)

        #print("oldPos: "+ str(robot.drivetrain.getPositions()))
        #print("newPos: "+str(targetPositions))
        self.heading = targetPositions
        robot.drivetrain.setPositions(targetPositions)

    def _calculateDisplacement(self, tdegrees):
        '''
        In order to avoid having a separate ticksPerDegree, we calculate it
        based on the width of the robot base.
        '''

        inchesPerDegree = math.pi * Config('DriveTrain/width') / 360
        totalDistanceInInches = tdegrees * inchesPerDegree

        return totalDistanceInInches * Config('DriveTrain/ticksPerInch') * 2


    def isFinished(self):
        #print("check finished: "+ str(self._finished))
        if self.heading == robot.drivetrain.getPositions():
            self._finished = True
            print("finished")
        return self._finished


    def end(self):
        #robot.drivetrain.stop()

        print("end")
