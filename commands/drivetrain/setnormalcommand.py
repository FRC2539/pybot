from wpilib.command import InstantCommand

import robot

class SetNormalCommand(InstantCommand):

    def __init__(self):
        super().__init__('Set Normal')

        self.requires(robot.drivetrain)

    def initialize(self):
        robot.drivetrain.setNormalSpeed()
