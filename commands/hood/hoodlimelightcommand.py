from wpilib.command import Command

import robot

class HoodLimelightCommand(Command):

    def __init__(self):
        super().__init__('Hood Limelight')

        self.requires(robot.hood)

        self.res = 0

    def initialize(self):
        pass

    def execute(self):
        if robot.hood.withinBounds() and robot.limelight.getTape():
            #if robot.limelight.get3D_Z() == 0.0:

            #self.res = robot.hood.benCalcAngle(robot.limelight.bensDistance())
            #else:
                #self.res = robot.hood.benCalcAngle(robot.limelight.get3D_Z())
            if robot.limelight.getA() > 1.289:
                self.res = robot.hood.setShootAngle(1.76491 * (robot.limelight.getA() ** 2) + 14)

            else:
                self.res = robot.hood.setShootAngle(1.76491 * (robot.limelight.getA() ** 2) + 11.5917)
        else:
            robot.hood.stopHood()

    def isFinished(self):
        return (abs(self.res - robot.hood.getPosition()) <= 1.0)

    def end(self):
        robot.hood.stopHood()
