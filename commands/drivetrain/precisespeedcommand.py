from wpilib.command import InstantCommand

import robot


class PreciseSpeedCommand(InstantCommand):

    def __init__(self):
        super().__init__('Precise Speed')

        self.requires(robot.drivetrain)

    def initialize(self):
        robot.drivetrain.toggleSlowSpeed()


