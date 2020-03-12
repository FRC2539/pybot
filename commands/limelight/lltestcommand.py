from wpilib.command import Command

import robot
import math

class llTestCommand(Command):

    def __init__(self):
        super().__init__('ll Test')

       #self.requires(robot.limelight)
        #self.requires(robot.drivetrain)
        self.requires(robot.turret)




    def initialize(self):
        robot.limelight.setPipeline(1)



    def execute(self):
        self.x = robot.limelight.getX()
        self.rotate = self.x * -.03
        if (abs(self.rotate) > .5):
            self.rotate = math.copysign(.5, self.rotate)
        robot.turret.move(self.rotate)


        print('Field Angle = '+str(robot.limelight.getFeildAngle()))
        print('distance = ' + str(robot.limelight.calcDistance()))
        print('x = '+ str(robot.limelight.calcXDistance()))
        print('y = '+ str(robot.limelight.calcYDistance()))


    def end(self):
        robot.limelight.setPipeline(0)
