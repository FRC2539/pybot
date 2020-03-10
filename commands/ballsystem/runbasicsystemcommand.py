from wpilib.command import Command

import robot


class RunBasicSystemCommand(Command):

    def __init__(self):
        super().__init__('Run Basic System')

        self.requires(robot.ballsystem)

    def initialize(self):
        robot.ballsystem.runAll()

    def end(self):
        robot.ballsystem.stopAll()
