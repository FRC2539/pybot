from wpilib.command import Command

import robot
import math

class TurretLimelightCommand(Command):

    def __init__(self):
        super().__init__('Turret Limelight')

        self.requires(robot.turret)
        self.turretOnTarget = False

    def initialize(self):
        robot.limelight.setPipeline(1)
        robot.ledsystem.onTarget = False
        self.count = 0

    def execute(self):
        #print('x ' + str(robot.limelight.getX()))
        self.x = robot.limelight.getX()
        #if self.x < 1:
            #self.rotate = self.x * -.15
        #else:
            #self.rotate = self.x * -.05
        self.rotate = self.x * -.03
        if (abs(self.rotate) > .5):
            self.rotate = math.copysign(.5, self.rotate)

        robot.turret.move(self.rotate)
        #print(str(self.rotate))

        if self.count >=4:
            robot.limelight.takeSnapShot()
        else:
            self.count = self.count + 1

        robot.ledsystem.onTarget = (robot.limelight.getX() <= 1.0)

    def end(self):
        robot.turret.stop()
        robot.limelight.setPipeline(0)
