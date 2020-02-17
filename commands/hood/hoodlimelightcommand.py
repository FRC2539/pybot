from wpilib.command import Command

import robot

class HoodLimelightCommand(Command):

    def __init__(self):
        super().__init__('Hood Limelight')

        self.requires(robot.hood)


    def initialize(self):
        robot.limelight.setPipeline(1)


    def execute(self):
        robot.limelight.updateNetworkTables()
        robot.hood.setShootAngle((1/2600)*(robot.limelight.calcDistance()-235)*(robot.limelight.calcDistance()-235) + 15.75)
        #if (robot.limelight.calcDistance()<120):
            #robot.hood.setShootAngle(38)
        #elif (robot.limelight.calcDistance()<140):
            #robot.hood.setShootAngle(37)
        #elif (robot.limelight.calcDistance()<160):
            #robot.hood.setShootAngle(36)
        #elif (robot.limelight.calcDistance()<180):
            #robot.hood.setShootAngle(35)
        #elif (robot.limelight.calcDistance()<200):
            #robot.hood.setShootAngle(34)
        #elif (robot.limelight.calcDistance()<220):
            #robot.hood.setShootAngle(33)
        #elif (robot.limelight.calcDistance()<260):
            #robot.hood.setShootAngle(32)
        #elif (robot.limelight.calcDistance()<280):
            #robot.hood.setShootAngle(33)
        #elif (robot.limelight.calcDistance()<300):
            #robot.hood.setShootAngle(34)
        #elif (robot.limelight.calcDistance()<320):
            #robot.hood.setShootAngle(35)
        #elif (robot.limelight.calcDistance()<340):
            #robot.hood.setShootAngle(36)
        #elif (robot.limelight.calcDistance()<360):
            #robot.hood.setShootAngle(37)
        #elif (robot.limelight.calcDistance()<380):
            #robot.hood.setShootAngle(38)
        #elif (robot.limelight.calcDistance()<400):
            #robot.hood.setShootAngle(39)
        #elif (robot.limelight.calcDistance()<420):
            #robot.hood.setShootAngle(40)
        #elif (robot.limelight.calcDistance()<440):
            #robot.hood.setShootAngle(41)
        #elif (robot.limelight.calcDistance()<460):
            #robot.hood.setShootAngle(42)
        #elif (robot.limelight.calcDistance()<480):
            #robot.hood.setShootAngle(43)



    def end(self):
        robot.limelight.setPipeline(0)
        robot.hood.stopHood()
