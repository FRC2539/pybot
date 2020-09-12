from wpilib.command import Command

import robot

class HoodLimelightCommand(Command):

    def __init__(self):
        super().__init__('Hood Limelight')

        self.requires(robot.hood)

        self.isHoodAligned = False
        self.res = False
        self.area = 0

    def initialize(self):
        #print('ran?')
        robot.limelight.setPipeline(0)

    def execute(self):
        if robot.hood.withinBounds() and robot.limelight.getTape():
            if robot.limelight.closeShot:
                self.isHoodAligned = robot.hood.alignAxises(robot.limelight.getY())
            else:
                self.isHoodAligned = robot.hood.alignAxisesFar(robot.limelight.getY(), robot.limelight.getA())
        else:
            robot.hood.stopHood()

    def isFinished(self):
        return self.res

    def end(self):
        #print('DONE?!?!?')
        robot.hood.stopHood()

        robot.limelight.setPipeline(1)

        self.isHoodAligned = False
        
