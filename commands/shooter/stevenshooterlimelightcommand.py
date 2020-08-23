from wpilib.command import Command

#from wpilib import Timer

import robot


class StevenShooterLimelightCommand(Command):

    def __init__(self):
        super().__init__('Steven Shooter Limelight')

        self.requires(robot.shooter)
        self.close = False

       # self.timer = Timer()


    def initialize(self):
        robot.limelight.setPipeline(0)


        #self.timer.start()



    def execute(self):
        self.speed = 4800 - 850 * robot.limelight.getA()
        if self.speed > 4800:
            self.speed = 4800

        robot.shooter.setRPM(self.speed)


    def end(self):
        robot.limelight.setPipeline(1)
        robot.shooter.stopShooter()
