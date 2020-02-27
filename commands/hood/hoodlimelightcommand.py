from wpilib.command import Command

import robot


class HoodLimelightCommand(Command):

    def __init__(self):
        super().__init__('Hood Limelight')
        self.requires(robot.hood)

    def initialize(self):
        robot.limelight.setPipeline(1)
        self.val = robot.hood.getLLHoodTuner()

    def execute(self):
        robot.limelight.updateNetworkTables()
        if robot.limelight.getTape():
            if robot.limelight.calcDistance() > 160:
                robot.hood.setShootAngle((1/2600)*(robot.limelight.calcDistance()-235)**2 + self.val) # was 15.75
            else:
                #robot.hood.setShootAngle((1/2600)*(robot.limelight.calcDistance()-235)*(robot.limelight.calcDistance()-235) + self.val + 3)
                robot.hood.setShootAngle(-2.3(robot.limelight.calcDistance()-120)**-3+26)
        else:
            robot.hood.stopHood()

    def end(self):
        robot.limelight.setPipeline(0)
        robot.hood.stopHood()