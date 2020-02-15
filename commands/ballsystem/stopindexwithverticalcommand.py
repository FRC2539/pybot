from wpilib.command import Command

import robot

class StopIndexWithVerticalCommand(Command):

    def __init__(self):
        super().__init__('Stop Index With Vertical')

        self.requires(robot.ballsystem)

    def initialize(self):
        robot.ballsystem.stopIndexWithVertical()
