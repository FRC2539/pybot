from wpilib.command import Command

import robot
import math


class SetFieldPositionCommand(Command):

    def __init__(self, x, y):
        super().__init__('Set Field Position')

        self.requires(robot.drivetrain)
        self.requires(robot.turret)

        self.gX = x
        self.gY = y


    def initialize(self):
        robot.limelight.setPipeline(1)


    def execute(self):
        # aims the turret
        self.x = robot.limelight.getX()
        self.rotate = self.x * -.03
        if (abs(self.rotate) > .5):
            self.rotate = math.copysign(.5, self.rotate)

        robot.turret.move(self.rotate)

        self.yD = robot.limelight.calcYDistance()
        self.xD = robot.limelight.calcXDistance()
        self.angle = robot.drivetrain.getAngle()


        self.cY = self.gY - self.yD
        self.cX = self.gX - self.xD
        print(str(self.cY))
        print(str(self.cX))
        self.rotate = (90-self.angle) * .01
        if abs(self.rotate) > (.2):
            print('rotate x ')
            robot.drivetrain.move(0,0,self.rotate)
        else:
            self.speed = self.cX * -.0075
            if self.cX > 10 :
                robot.drivetrain.move(0,self.speed,0)
                print('x')
            else:
                self.rotate = (180-self.angle) * -.01
                if abs(self.rotate) > (.01):
                    robot.drivetrain.move(0,0,self.rotate)
                    print('rotate y')
                else:
                    self.speed = self.cY *.0075
                    print('y')
                    robot.drivetrain.move(0,self.speed,0)



    def end(self):
        robot.limelight.setPipeline(0)
        robot.drivetrain.move(0,0,0)
        robot.turret.stop()
