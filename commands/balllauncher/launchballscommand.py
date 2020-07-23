from wpilib.command import Command

import robot

class LaunchBallsCommand(Command):

    def __init__(self):
        super().__init__('Launch Balls')

        self.requires(robot.balllauncher)

    def initialize(self):
        robot.balllauncher.launchBalls()

    def end(self):
        robot.balllauncher.stopLauncher()
