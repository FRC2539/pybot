from wpilib.command.command import Command

import robot

class MovePercentCommand(Command):

    def __init__(self, y=.2):
        super().__init__('Move Percent')

        self.requires(robot.drivetrain)
        self.y = y

    def initialize(self):
        robot.drivetrain.move(0, self.y, 0)


    def end(self):
        robot.drivetrain.stop()
