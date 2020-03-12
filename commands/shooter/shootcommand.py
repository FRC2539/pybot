from wpilib.command import Command

from networktables import NetworkTables

import robot

class ShootCommand(Command):

    def __init__(self, rpm):
        super().__init__('Shoot')
        self.requires(robot.shooter)

        self.rpm = rpm

        self.table = NetworkTables.getTable('Shooter')

    def initialize(self):
        robot.shooter.setRPM(self.rpm)
        robot.shooter.setGoalNetworkTables(self.rpm)
        robot.ledsystem.flashRed()

    def execute(self):
        currentRPM = robot.shooter.getRPM()

        if currentRPM >= self.rpm - 200:
            robot.ledsystem.setRed()
        else:
            robot.ledsystem.flashRed()

        self.table.putNumber('ShooterRPM', currentRPM)

    def end(self):
        robot.shooter.stop()
        robot.shooter.zeroNetworkTables()
        robot.ledsystem.turnOff()
