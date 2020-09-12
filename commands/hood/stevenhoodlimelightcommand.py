from wpilib.command import Command

import robot


class StevenHoodLimelightCommand(Command):

    def __init__(self):
        super().__init__('Steven Hood Limelight')

        self.requires(robot.hood)


    def initialize(self):
        robot.limelight.setPipeline(1)


    def execute(self):
        if robot.limelight.getTape():
            if (robot.limelight.getA() > 1.289):
                robot.hood.setShootAngle(1.76491 * (robot.limelight.getA() * robot.limelight.getA()) + 20 + robot.hood.getAdjustment())
            else:
                robot.hood.setShootAngle(1.76491 * (robot.limelight.getA() * robot.limelight.getA()) + 20 +robot.hood.getAdjustment())

        else:
            robot.hood.stopHood()
    def end(self):
        robot.limelight.setPipeline(0)
        robot.hood.stopHood()
