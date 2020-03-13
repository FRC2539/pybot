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
        self.tx = 0
        self.ty = 0
        self.deltaX = 0
        self.deltaY = 0


    def execute(self):
        if robot.turret.getPosition() > 825 and robot.turret.getPosition() < 875:
            self.x = robot.limelight.getX()
            self.rotate = self.x * .05
            if (abs(self.rotate) > .5):
                self.rotate = math.copysign(.5, self.rotate)
            if abs(self.rotate) < .07 and abs(self.x) > 1:
                self.rotate = math.copysign(.07, self.rotate)
            if abs(self.x) < 1:
                self.rotate = 0
                #bens move
                self.x = robot.limelight().calcXDistance()
                self.y = robot.limelight().calcYDistance()
                self.deltaX = self.tx - self.x
                self.deltaY = self.ty - self.y
                self.angle = math.degrees(math.atan(self.deltaX/self.deltaY))
                self.deltaD = math.sqrt(self.deltaX * self.deltaX + self.deltaY * self.deltaY)
            else:
                robot.drivetrain.move(0,0,self.rotate)
        else:
            robot.turret.setPosition(850)





    def end(self):
        robot.limelight.setPipeline(0)
