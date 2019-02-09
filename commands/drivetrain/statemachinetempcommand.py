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

        robot.drivetrain.setSpeedLimit(600)

        self._checkforTape()

        #robot.drivetrain.setPositions(self.targetPositions)




    def execute(self):
        #print("here")

        if self.sock != -1:
            data, addr = self.sock.recvfrom(1024) # buffer size is 1024 bytes
            print("1 received message:" + str(data))
            self.tmessage = data.decode("utf-8")
            self.message = self.tmessage.split(",")
            self.tapeFound = self.message[0].split(":")[1]
            self.tapeX = float(self.message[1].split(":")[1])
            self.tapeDistance = float(self.message[2].split(":")[1])

            #print("tf-"+str(tapeFound))
            #print("tx: "+str(tapeX))
            print("td: "+str(self.tapeDistance))

            if self.tapeFound == "True":
                #print("tape")
                self.offset = self.tapeX #(self.tapeX - (640/2))/640 * 5
                #print("offset: "+str(offset))
                #if tapeDistance <= 4:
                #    offset = 0
                #elif offset <= 5 and offset >= -5:
                #    offset = 0

                if self.tapeDistance <= 70:
                    self.tapeDistance -= 70
                    #self.moveDistance = 0
                    #self.offset = 0
                    #print("too close, stopping")
                    #robot.drivetrain.stop()
                else:


                    self.offset = 0
                    #moveDistance = (tapeDistance - 60) * Config('DriveTrain/ticksPerInch')
                    self.moveDistance = (6) * Config('DriveTrain/ticksPerInch')
                    #print("pivot and move: "+str(offset)+"% "+str(moveDistance))



                    #self._pivotandmove(offset, moveDistance)

                    self.targetPositions = []

                    md = 90 * Config('DriveTrain/ticksPerInch')#moveDistance
                    self.x = 0
                    for position in robot.drivetrain.getPositions():
                        if self.x % 2 == 0:
                            self.targetPositions.append(position + md)
                        else:
                            self.targetPositions.append(position - md)
                        self.x += 1

                    #print("moving: "+ str(moveDistance / Config('DriveTrain/ticksPerInch')))
                    #print("otarget-"+str(robot.drivetrain.getPositions()))
                    #print("ntarget-"+str(self.targetPositions))

                    robot.drivetrain.setSpeedLimit(1200)

                    if self.num >= 10:
                        robot.drivetrain.setPositions(self.targetPositions)
                        self.num = 0

                self.num += 1

            else:
                print("no tape")
                #robot.drivetrain.stop()








    def _checkforTape(self):
        if self.sock != -1:

            try:
                #print("while")
                data, addr = self.sock.recvfrom(1024) # buffer size is 1024 bytes
                tmessage = data.decode("utf-8")
                print("received message:" + str(tmessage))





            except Exception as seriousbusiness:
            #except:
                print("error- "+ str(seriousbusiness))
                #print("udp message error")

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
        offset = self._calculateDisplacement(tdegrees) * self.direction
        targetPositions = []
        sign = 1
        for i, position in enumerate(robot.drivetrain.getPositions()):
            side = i % 2
            if self.pivotSide == side:
                position += offset
                position -= tdistance
                position = position * sign
                sign *= -1
            else:
                position += tdistance
                position = position * sign
                sign *= -1

            targetPositions.append(position)

        print(robot.drivetrain.getPositions())
        print("newPos- "+str(targetPositions))

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

        return self._finished


    def end(self):
        #robot.drivetrain.stop()

        print("end")
