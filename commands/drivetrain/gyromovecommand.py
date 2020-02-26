from wpilib.command import Command

import robot


class GyroMoveCommand(Command):

    def __init__(self):
        super().__init__('Gyro Move')

        self.requires(robot.drivetrain)


    def initialize(self):
        pass


    def execute(self):
        pass


    def end(self):
        pass
