from wpilib.command import Command

import robot

class TurretLimelightCommand(Command):

    def __init__(self):
        super().__init__('Turret Limelight')

        self.requires(robot.turret)


    def initialize(self):
        robot.limelight.setPipeline(1)



    def execute(self):
        self.rotate = robot.limelight.getX()*-.035
        robot.turret.move(self.rotate)
        print('self.rotate')



    def end(self):
        robot.limelight.setPipeline(0)
