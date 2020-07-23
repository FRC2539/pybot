from wpilib.command import Command

import robot

class SpitBallsCommand(Command):

    def __init__(self):
        super().__init__('Spit Balls')

        self.requires(robot.shooter)

    def initialize(self):
        robot.shooter.setRPM(1000)

    def end(self):
        robot.shooter.stopShooter()
