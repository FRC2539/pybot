from wpilib.command.command import Command

import robot

class ShooterLimelightCommand(Command):

    def __init__(self):
        super().__init__('Shooter Limelight')

        self.requires(robot.shooter)
        self.requires(robot.limelight)


    def initialize(self):
        robot.limelight.setPipeline(1)


    def execute(self):
        robot.limelight.calcDistance()


    def end(self):
        robot.limelight.setPipeline(0)
