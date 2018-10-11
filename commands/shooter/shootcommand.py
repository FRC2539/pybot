from wpilib.command.command import Command

import robot

class ShootCommand(Command):

    def __init__(self):
        super().__init__('Shoot')

        self.requires(robot.shooter)

    def initialize(self):
        robot.shooter.shoot()

    def end(self):
        robot.shooter.stop()
