from wpilib.command import Command

import robot

class BoogityCommand(Command):

    def __init__(self):
        super().__init__('Boogity')

        self.requires(robot.drivetrain)

    def initialize(self):
        robot.drivetrain.playM()

    def end(self):
        robot.drivetrain.stopM()
