from wpilib.command.command import Command

import robot

class SlowShootCommand(Command):

    def __init__(self):
        super().__init__('Slow Shoot')

        self.requires(robot.shooter)


    def initialize(self):
        robot.shooter.slowShoot()

    def end(self):
        robot.shooter.stop()
