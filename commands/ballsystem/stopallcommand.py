from wpilib.command import Command

import robot

class StopAllCommand(Command):

    def __init__(self):
        super().__init__('Stop All')

        self.requires(robot.ballsystem)

    def initialize(self):
        robot.ballsystem.stopAll()
