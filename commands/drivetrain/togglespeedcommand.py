from wpilib.command.command import Command
from custom.config import Config

import robot

class ToggleSpeedCommand(Command):

    def __init__(self):
        super().__init__('Toggle Speed')

        self.requires(robot.drivetrain)


    def initialize(self):
        robot.drivetrain.toggleSpeed()

