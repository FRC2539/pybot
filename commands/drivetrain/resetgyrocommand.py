from wpilib.command import Command

import robot


class ResetGyroCommand(Command):

    def __init__(self):
        super().__init__('Reset Gyro')

        self.requires(robot.drivetrain)


    def initialize(self):
        pass


    def execute(self):
        pass


    def end(self):
        pass
