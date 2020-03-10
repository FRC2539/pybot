from wpilib.command import Command

import robot


class PullWinchCommand(Command):

    def __init__(self):
        super().__init__('Pull Winch')

        self.requires(robot.winch)
        self.requires(robot.ledsystem)
        #self.requires(robot.drivetrain)

    def initialize(self):
        robot.winch.retract()
        robot.ledsystem.rainbowLava()

    def end(self):
        robot.winch.stopWinch()
        robot.ledsystem.turnOff()

