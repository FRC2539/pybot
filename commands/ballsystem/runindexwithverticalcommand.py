from wpilib.command import Command

import robot

class RunIndexWithVerticalCommand(Command):

    def __init__(self):
        super().__init__('Run Index With Vertical')

        self.requires(robot.ballsystem)

    def initialize(self):
        robot.ballsystem.runVerticalConveyor()

    def end(self):
        robot.ballsystem.stopVerticalConveyor()
