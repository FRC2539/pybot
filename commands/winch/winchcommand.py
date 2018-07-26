from wpilib.command.command import Command

import robot

class WinchCommand(Command):

    def __init__(self, speed):
        super().__init__('winch')

        self.requires(robot.winch)
        self.speed = speed



    def initialize(self):
        robot.winch.moveWinch(self.speed)
        print('Start winch')


    def execute(self):
        pass


    def end(self):
        robot.winch.moveWinch(0)
        print('Stop winch')
