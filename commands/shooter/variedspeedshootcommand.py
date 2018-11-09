from wpilib.command.command import Command

import robot

class VariedSpeedShootCommand(Command):

    def __init__(self):
        super().__init__('Varied Speed Shoot')

        self.requires(robot.shooter)

    def initialize(self):
        robot.shooter.variedShoot()

    def end(self):
        robot.shooter.stop()
