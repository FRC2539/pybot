from wpilib.command.command import Command
#from magicbot import StateMachine
#from magicbot.magicrobot import MagicRobot
#from magicbot.state_machine import AutonomousStateMachine

#from magicbot.state_machine import state

#from commands.drivetrain.pivotcommand import PivotCommand

#from commands.drivetrain.pivotcommand import PivotCommand

from .movecommand import MoveCommand

from networktables import NetworkTables

from custom.config import Config

from commands.network.alertcommand import AlertCommand

import math

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

        self.direction = 1

        # 0 = Left Side, 1 = Right Side
        self.pivotSide = 0
        if self.degrees < 0:
            self.pivotSide = 1

        if reverse:
            self.pivotSide = abs(self.pivotSide - 1)

    def execute(self):

        if self.num >= 50:
            #self.stateMachineTable.putNumber('returnNumber', self.num)

            if Config('cameraInfo/tapeFound', False):



                robot.drivetrain.stop()

                tapeX = Config('cameraInfo/tapeX', -1)
                print("f-"+str(tapeX))
                offset = (tapeX - (480/2))/480 * 52
                print("offset:"+str(offset))
                self._pivot(offset)
                '''
                if tapeX <= 290:
                    print("left-"+str(int(tapeX)))
                    #offset = -((260 - tapeX)/15)
                    offset = (tapeX - (480/2))/480 * 72
                    print("offset:"+str(-offset))
                    self._pivot(-offset)


                elif tapeX >=325:
                    print("right-"+str(int(tapeX)))
                    #offset = (tapeX - 310)/15
                    offset = (tapeX - (480/2))/480 * 72
                    print("offset:"+str(offset))
                    self._pivot(offset)


                else:
                    print("centered"+(str(int(tapeX))))

                '''

            #else:
                #self._pivot(self.degrees)

                #print("turning")
            self.num = 0
        else:
            self.num += 1

    def _pivot(self, tdegrees):
        offset = self._calculateDisplacement(tdegrees) * self.direction
        targetPositions = []
        for i, position in enumerate(robot.drivetrain.getPositions()):
            side = i % 2
            if self.pivotSide == side:
                position += offset

            targetPositions.append(position)

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
