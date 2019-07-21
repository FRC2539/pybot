from wpilib.command.command import Command

import robot

class MediumShootCommand(Command):

    def __init__(self):
        super().__init__('Medium Shoot')

        self.requires(robot.shooter)


    def initialize(self):
        robot.shooter.mediumShoot()


    def end(self):
        robot.shooter.stop()
