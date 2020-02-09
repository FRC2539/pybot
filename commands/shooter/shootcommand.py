from wpilib.command import Command

import robot

class ShootCommand(Command):

    def __init__(self):
        super().__init__('Shoot')

        self.requires(robot.shooter)

    def initialize(self):
        robot.shooter.setRPM()

    def execute(self):
        robot.shooter.updateNetworkTables()
        print('RPM: ' + str(robot.shooter.getRPM()))

    def end(self):
        robot.shooter.stop()
        robot.shooter.zeroNetworkTables()
