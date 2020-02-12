from wpilib.command.command import Command

import robot

class ReverseShooterCommand(Command):

    def __init__(self):
        super().__init__('Reverse Shooter')

        self.requires(robot.shooter)


    def initialize(self):
        pass


    def execute(self):
        pass


    def end(self):
        pass
