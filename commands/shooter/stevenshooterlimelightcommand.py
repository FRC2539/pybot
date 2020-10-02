from wpilib.command import Command

#from wpilib import Timer

import robot


class StevenShooterLimelightCommand(Command):

    def __init__(self):
        super().__init__('Steven Shooter Limelight')

        self.requires(robot.shooter)
        self.close = False

    def initialize(self):
        robot.shooter.atGoal = False
        robot.limelight.setPipeline(0)

    def execute(self):
        self.speed = 4800 - 850 * robot.limelight.getA()
        if self.speed > 4800:
            self.speed = 4800

        self.speed = 6000

        robot.shooter.setRPM(self.speed)
        
        #robot.shooter.updateNetworkTables()
        
        #print('rpm ' + str(robot.shooter.getRPM()))
        
        if abs(robot.shooter.getRPM()) + 300 >= self.speed: # Only needs to pass this once. Adds a tolerance of 30, in case it hovers below.
            robot.shooter.atGoal = True

    def end(self):
        robot.shooter.atGoal = False
        robot.limelight.setPipeline(1)
        robot.shooter.stopShooter()
        robot.shooter.zeroNetworkTables()
