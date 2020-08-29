from wpilib.command import Command

import robot


class TestCommand(Command):

    def __init__(self):
        super().__init__('Test')

        self.requires(robot.drivetrain)


    def initialize(self):
        pass


    def execute(self):
        robot.drivetrain.setSpeeds(1000,1000)


    def end(self):
        pass
