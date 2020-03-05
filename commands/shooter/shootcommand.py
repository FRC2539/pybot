from wpilib.command import Command

import robot

class ShootCommand(Command):

    def __init__(self, rpm):
        super().__init__('Shoot')
        self.requires(robot.shooter)

        self.rpm = rpm

    def initialize(self):
        robot.shooter.setRPM(self.rpm)
        robot.shooter.setGoalNetworkTables()
        robot.ledsystem.flashRed()

    def execute(self):
        if robot.shooter.getRPM() >= self.rpm - 200:
            robot.ledsystem.setRed()
        else:
            robot.ledsystem.flashRed()

    def end(self):
        robot.shooter.stop()
        robot.shooter.zeroNetworkTables()
        robot.ledsystem.turnOff()
