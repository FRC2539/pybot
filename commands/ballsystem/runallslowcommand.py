from wpilib.command import Command

import robot


class RunAllSlowCommand(Command):

    def __init__(self):
        super().__init__('Run All Slow')

        self.requires(robot.ballsystem)

    def initialize(self):
        robot.ballsystem.runLowSlowAndVertical()

    def end(self):
        robot.ballsystem.stopAll()
