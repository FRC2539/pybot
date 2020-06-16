from wpilib.command import Command

import robot
import math

class llTestCommand(Command):

    def __init__(self):
        super().__init__('ll Test')

        self.requires(robot.drivetrain)
        self.requires(robot.turret)

    def initialize(self):
        robot.limelight.setPipeline(1)
        self.tx = -65
        self.ty = 180
        self.deltaX = 0
        self.deltaY = 0
        self.finished = False
        self.measured = False
        self.aimed = False
        self.turret = False


    def execute(self):

        if not self.turret:
            if robot.turret.getPosition() > 900:
                self.turret = True
            robot.turret.setPosition(975)
            #print('turret')


        elif not self.aimed:
            robot.turret.stop()
            self.x = robot.limelight.getX()
            if abs(self.x) < 2 and robot.limelight.getTape:
                self.aimed = True
            self.rotate = self.x * .05
            if (abs(self.rotate) > .5):
                self.rotate = math.copysign(.5, self.rotate)
            if abs(self.rotate) < .15 and abs(self.x) > 2:
                self.rotate = math.copysign(.15, self.rotate)
            robot.drivetrain.move(0,0,self.rotate)
            #print('aim')

        elif not self.measured:
            self.x = robot.limelight.calcXDistance()
            self.y = robot.limelight.calcYDistance()
            self.deltaX = self.tx - self.x
            self.deltaY = self.ty - self.y
            self.angle = math.degrees(math.atan(self.deltaX/self.deltaY))
            self.deltaD = math.sqrt(self.deltaX * self.deltaX + self.deltaY * self.deltaY)
            self.measured = True
            if self.angle < 0 :
                self.angle = self.angle + 360
            if self.angle > 360 :
                self.angle = self.angle - 360
            ##print('measure')

        elif not self.finished:
            self.finished= robot.drivetrain.turnThenMove(self.deltaD, self.angle)
            #print('finish')

        self._isFinished = self.finished


    def isFinished(self):
        return self._isFinished



    def end(self):
        robot.limelight.setPipeline(0)
        robot.drivetrain.stop()
        robot.turret.stop()

        robot.drivetrain.turnSet = False
        robot.drivetrain.turnDone = False
        robot.drivetrain.moveSet = False
        robot.drivetrain.moveDone = False
