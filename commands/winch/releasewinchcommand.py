from wpilib.command import Command

import robot


class ReleaseWinchCommand(Command):

    def __init__(self):
        super().__init__('Release Winch')

        self.requires(robot.winch)

    def initialize(self):
        robot.winch.loosen()

    def end(self):
        robot.winch.stop()
