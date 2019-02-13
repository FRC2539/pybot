from wpilib.command.command import Command

from custom.config import Config

import robot
from subsystems import basedrive

class NewRampingSpeedCommand(Command):

    def __init__(self, distance, endSpeed):
        super().__init__('New Ramping Speed')

        self.requires(robot.drivetrain)
        self.distance = distance
        self.endSpeed = endSpeed
        self._isFinished = False

    def getSpeedLimit(self):
        return robot.drivetrain.speedLimit

    def initialize(self):
        self.count = 0
        self.ticksPerInch = 233.5
        self.newPos = []

        self.currentPos = robot.drivetrain.getPositions()

        self.maxSpeed = 600 #robot.drivetrain.speedLimit
        self.oldSpeed = robot.drivetrain.speedLimit

        self.speedDifferential = abs(self.maxSpeed / self.distance)

        print('len ' + str(len(self.currentPos)))
        print('old positions' + str(self.currentPos))

        for i in self.currentPos:
            inchesinTicks = self.ticksPerInch * self.distance #* self.distance




            if self.distance < 0:
                if i == self.currentPos[1]:
                    print('why')
                    i *= -1
                self.newPos.append(i - inchesinTicks)

            else:
                if i == self.currentPos[1]:
                    print('hmm')
                    i *= 1
                    self.newPos.append(i - inchesinTicks)

                else:
                    self.newPos.append(i + inchesinTicks)

        self.currentPos = self.newPos
        print('New positions: ' + str(self.currentPos))

        # Moving

        self.speed = robot.drivetrain.speedLimit

    def execute(self):

        speedLimit = self.getSpeedLimit()

        val = robot.drivetrain.setRampingPositions(self.newPos, self.distance, self.endSpeed, speedLimit)

        if val:
            self._isFinished= True
    """
        print('started execute')


        try:
            robot.drivetrain.setSpeedLimit(self.maxSpeed)
        except ValueError:


        #self.maxSpeed = 2500

        if self.maxSpeed < 50:
            self._isFinished = True

            #   self.count += 1

    """

    def isFinshed(self):
        return self._isFinished

    def end(self):
        print('Done')
        robot.drivetrain.stop()
       # robot.drivetrain.setSpeedLimit(self.oldSpeed)
