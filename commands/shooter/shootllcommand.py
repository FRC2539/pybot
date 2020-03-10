from wpilib.command import Command

import robot


class ShootllCommand(Command):

    def __init__(self):
        super().__init__('Shootll')

        self.requires(robot.shooter)


    def initialize(self):
        pass


    def execute(self):
        pass


    def end(self):
        pass
