from wpilib.command import Command

import robot

class HoodLimelightCommand(Command):

    def __init__(self):
        super().__init__('Hood Limelight')

        self.requires(robot.hood)

        self.res = False

    def initialize(self):
        pass

    def execute(self):
        if robot.hood.withinBounds() and robot.limelight.getTape():
            if robot.limelight.get3D_Z() == 0.0:
                self.res = robot.hood.benCalcAngle(robot.limelight.bensDistance())
            else:
                self.res = robot.hood.benCalcAngle(robot.limelight.get3D_Z())

        else:
            robot.hood.stopHood()

    def isFinished(self):
        return self.res

    def end(self):
        robot.hood.stopHood()
