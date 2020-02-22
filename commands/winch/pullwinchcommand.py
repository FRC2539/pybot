from wpilib.command import Command

import robot


class PullWinchCommand(Command):

    def __init__(self):
        super().__init__('Pull Winch')

        self.requires(robot.winch)

    def initialize(self):
        robot.winch.retract()

    def end(self):
        robot.winch.stop()
