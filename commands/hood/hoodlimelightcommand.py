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
        robot.hood.setShootAngle((1/2600)*(robot.limelight.calcDistance()-235)*(robot.limelight.calcDistance()-235) + 13) # was 15.75


    def end(self):
        robot.limelight.setPipeline(0)
        robot.hood.stopHood()
