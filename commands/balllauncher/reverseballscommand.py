from wpilib.command import Command

import robot

class ReverseBallsCommand(Command):

    def __init__(self):
        super().__init__('Reverse Balls')

        self.requires(robot.balllauncher)

    def initialize(self):
        robot.balllauncher.reverseBalls()

    def end(self):
        robot.balllauncher.stopLauncher()
