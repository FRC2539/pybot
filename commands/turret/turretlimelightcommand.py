from wpilib.command import Command

import robot
import math

class TurretLimelightCommand(Command):

    def __init__(self):
        super().__init__('Turret Limelight')

        self.requires(robot.turret)

    def initialize(self):
        robot.limelight.setPipeline(0)
        robot.turret.onTarget = False

    def execute(self):
        self.x = robot.limelight.getX() + robot.turret.getAdjustment()
        self.rotate = self.x * 0.03
        self.speedLimit = .3
        if (abs(self.rotate) > self.speedLimit):
            self.rotate = math.copysign(self.speedLimit, self.rotate)

        #print('r ' + str(self.rotate))

        robot.turret.move(self.rotate)

        robot.turret.onTarget = (robot.limelight.getX() <= 1.0)
        robot.turret.updateNetworkTables()

    def end(self):
        robot.turret.stop()
        robot.turret.onTarget = False
        robot.limelight.setPipeline(1)
