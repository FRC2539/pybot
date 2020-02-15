from wpilib.command import Command

import robot

class RunAllCommand(Command):

    def __init__(self):
        super().__init__('Run All')

        self.requires(robot.ballsystem)

    def initialize(self):
        robot.ballsystem.runAll()

    def end(self):
        robot.ballsystem.stopAll()
