from wpilib.command import Command

import robot

class ClearJamCommand(Command):

    def __init__(self):
        super().__init__('Reverse Chamber')

        self.requires(robot.ballsystem)

    def initialize(self):
        robot.ballsystem.reverseAll()

    def end(self):
        robot.ballsystem.stopAll()
