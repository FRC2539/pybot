from wpilib.command import Command

import robot


class HoodLimelightCommand(Command):

    def __init__(self):
        super().__init__('Hood Limelight')
        self.requires(robot.hood)
        #self.onTarget = False

    def initialize(self):
        robot.limelight.setPipeline(1)
        #self.val = robot.hood.getLLHoodTuner()

    def execute(self):
        #print('distance ' + str(robot.limelight.calcDistance()))
        robot.limelight.updateNetworkTables()
        if robot.limelight.getTape():
            if robot.limelight.getA() > 1.289 :
                robot.hood.setShootAngle(1.76491*(robot.limelight.getA()*robot.limelight.getA())+14)
            #elif robot.limelight.getA()<.75:
                #robot.hood.setShootAngle(1.76491*(robot.limelight.getA()*robot.limelight.getA())+12.5917)
            else:
                robot.hood.setShootAngle(1.76491*(robot.limelight.getA()*robot.limelight.getA())+11.5917)
            #if robot.limelight.calcDistance() > 160:
                #robot.hood.setShootAngle((1/2600)*(robot.limelight.calcDistance()-235)**2 + self.val) # was 15.75
            #else:
                #robot.hood.setShootAngle((1/2600)*(robot.limelight.calcDistance()-235)**2 + self.val + ((160 - robot.limelight.calcDistance()) / 3))
                #robot.hood.setShootAngle(-2.3 * (robot.limelight.calcDistance()-120)**-3 + 26)
                # and abs(robot.hood.targetpos - robot.hood.getPosition() <= 5.0)
        else:
            robot.hood.stopHood()

    def end(self):
        robot.limelight.setPipeline(0)
        robot.hood.stopHood()
