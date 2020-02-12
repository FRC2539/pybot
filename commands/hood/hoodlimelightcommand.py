from wpilib.command.command import Command

import robot

class HoodLimelightCommand(Command):

    def __init__(self):
        super().__init__('Hood Limelight')

        self.requires(robot.hood)
        self.requires(robot.limelight)


    def initialize(self):
        robot.limelight.setPipeline(1)


    def execute(self):
        if (robot.limelight.calcDistance()<120):
            robot.hood.OpenLoopSetPos(38)



    def end(self):
        robot.limelight.setPipeline(0)
