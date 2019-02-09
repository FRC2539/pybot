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

    def initialize(self):
        self.count = 0
        self.ticksPerInch = 233.5
        self.newPos = []

        self.currentPos = robot.drivetrain.getPositions()

        self.maxSpeed = robot.drivetrain.speedLimit
        self.oldSpeed = robot.drivetrain.speedLimit

        self.speedDifferential = abs(self.maxSpeed / self.distance)

        print('len ' + str(len(self.currentPos)))
        print('old positions' + str(self.currentPos))

        for i in self.currentPos:
            inches = self.ticksPerInch * self.distance




            if self.distance < 0:
                if i == self.currentPos[1]:
                    print('why')
                    i *= -1
                self.newPos.append(i - inches)

            else:
                if i == self.currentPos[1]:
                    print('hmm')
                    i *= 1
                    self.newPos.append(i - inches)

                else:
                    self.newPos.append(i + inches)

        self.currentPos = self.newPos
        print('New positions: ' + str(self.currentPos))

        # Moving
        robot.drivetrain.setPositions(self.currentPos)
        print('Started Moving')

    def execute(self):
        if self.count >= 30:
            self.maxSpeed = 600#-= self.speedDifferential

            try:
                robot.drivetrain.setSpeedLimit(self.maxSpeed)
            except ValueError:
                self.maxSpeed = 2500

            if self.maxSpeed < 100:
                self._isFinished = True

                #   self.count += 1
        else:
            self.count += 1


    def isFinshed(self):
        return self._isFinished

    def end(self):
        print('Done')
        robot.drivetrain.stop()
        robot.drivetrain.setSpeedLimit(self.oldSpeed)
