from wpilib.command.command import Command

import robot

class DonutsCommand(Command):

    def __init__(self):
        super().__init__('Donuts')

        self.requires(robot.drivetrain)


    def initialize(self):
        if robot.drivetrain.isFieldOriented:
            robot.drivetrain.toggleFieldOrientation()


    def execute(self):
        robot.drivetrain.move(1, 0.4, -0.6)


    def end(self):
        robot.drivetrain.stop()
