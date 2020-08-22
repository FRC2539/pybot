from wpilib.command import Command

import robot

class HoodLimelightCommand(Command):

    def __init__(self):
        super().__init__('Hood Limelight')

        self.requires(robot.hood)

        self.res = False
        self.area = 0

    def initialize(self):
        print('ran?')
        robot.limelight.setPipeline(0)

    def execute(self):
        if robot.hood.withinBounds() and robot.limelight.getTape():
            #if robot.limelight.get3D_Z() == 0.0:
                #self.res = robot.hood.benCalcAngle(robot.limelight.bensDistance())
            #else:
                #self.res = robot.hood.ben  CalcAngle(robot.limelight.get3D_Z())
            self.area = robot.limelight.getA()

            print('aaaa ' + str(self.area))

            if abs(abs(self.area) - 0.6) < 0.05: # adjust based off of measurements.
                self.res = robot.hood.mobileHoodControl(robot.limelight.getY(), self.area)

            else:
                self.res = robot.hood.mobileHoodControl(robot.limelight.getY())
        else:
            robot.hood.stopHood()

    def isFinished(self):
        return self.res

    def end(self):
        print('DONE?!?!?')
        robot.hood.stopHood()

        robot.limelight.setPipeline(1)

        self.proceed = False
