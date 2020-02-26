from wpilib.command import Command

import robot


class DriveBaseLimelightCommand(Command):

    def __init__(self):
        super().__init__('Drive Base Limelight')

        self.requires(robot.drivetrain)


    def initialize(self):
        robot.limelight.setPipeline(1)


    def execute(self):
        self.rotate = robot.limelight.getX() * .035
        if (abs(self.rotate) > .3):
            self.rotate = math.copysign(.3, self.rotate)
        robot.drivetrain.move(0,0,self.rotate)


    def end(self):
        robot.drivetrain.stop()
        robot.limelight.setPipeline(0)
