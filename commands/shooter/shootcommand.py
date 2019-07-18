from wpilib.command.command import Command

import robot

class ShootCommand(Command):

    def __init__(self):
        super().__init__('Shoot')

        self.requires(robot.shooter)


    def initialize(self):
        pass


    def execute(self):
        pass


    def end(self):
        pass
