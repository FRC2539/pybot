from wpilib.command import Command

import robot

class ShootCommand(Command):

    def __init__(self):
        super().__init__('Shoot')

        self.requires(robot.shooter)

    def initialize(self):
        robot.shooter.setRPM()
        robot.shooter.updateCheck()
        robot.shooter.setGoalNetworkTables()

    def execute(self):
        robot.shooter.sensorCount()
        robot.shooter.updateNetworkTables()

    def end(self):
        robot.shooter.stop()
        robot.shooter.zeroNetworkTables()
