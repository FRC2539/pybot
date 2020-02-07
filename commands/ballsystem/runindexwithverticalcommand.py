from wpilib.command import Command

import robot

class RunIndexWithVerticalCommand(Command):

    def __init__(self):
        super().__init__('Run Index With Vertical')

        self.requires(robot.ballsystem)

    def initialize(self):
        robot.ballsystem.runIndexWithVertical()

    def end(self):
        robot.ballsystem.stopIndexWithVertical()
