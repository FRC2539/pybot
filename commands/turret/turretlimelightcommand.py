from wpilib.command import Command

import robot
import math

class TurretLimelightCommand(Command):

    def __init__(self):
        super().__init__('Turret Limelight')

        self.requires(robot.turret)


    def initialize(self):
        robot.limelight.setPipeline(1)



    def execute(self):
        self.rotate = robot.limelight.getX() * -.035
        if (abs(self.rotate) > .3):
            self.rotate = math.copysign(.3, self.rotate)
        robot.turret.move(self.rotate)
        print(str(self.rotate))



    def end(self):
        robot.turret.stop()
        robot.limelight.setPipeline(0)
