from wpilib.command import Command

import robot

class TurretLimelightCommand(Command):

    def __init__(self):
        super().__init__('Turret Limelight')

        self.requires(robot.turret)
        self.requires(robot.limelight)


    def initialize(self):
        robot.limelight.setPipeline(1)



    def execute(self):
        self.rotate = robot.limelight.getX()*.03
        robot.turret.move(self.rotate)


    def end(self):
        robot.limelight.setPipeline(0)
