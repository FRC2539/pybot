from wpilib.command import Command
from commands.drivetrain.turncommand import TurnCommand

from wpilib import Timer

import robot

class ShooterLimelightCommand(Command):

    def __init__(self):
        super().__init__('Shooter Limelight')

        self.requires(robot.shooter)
        self.close = False

        self.timer = Timer()

    def initialize(self):
        robot.limelight.setPipeline(1)
        robot.ledsystem.setRed()


        self.timer.start()
        self.secondCounter = 0


    def execute(self):

        self.speed = 4800 - 850 * robot.limelight.getA()
        if self.speed > 4800:
            self.speed = 4800
        if self.timer.hasElapsed(self.secondCounter):
            robot.shooter.updateNetworkTables(robot.shooter.getRPM())
            self.secondCounter += 2
            robot.shooter.setGoalNetworkTables(self.speed)


        #print("fart")
        robot.shooter.setRPM(self.speed)
        #print("beans")

        #TurnCommand(500)



    def end(self):
        robot.ledsystem.turnOff()
        robot.limelight.setPipeline(0)
        robot.shooter.stop()

        self.timer.stop()
        self.timer.reset()

        robot.shooter.zeroNetworkTables()
