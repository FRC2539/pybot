from wpilib.command.command import Command

import robot

class RaiseBallCommand(Command):

    def __init__(self):
        super().__init__('Raise Ball')

        self.requires(robot.elevator)


    def initialize(self):
        robot.elevator.fastElevate()


    def end(self):
        robot.elevator.stop()
