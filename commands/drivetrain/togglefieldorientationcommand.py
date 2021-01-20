from wpilib.command import InstantCommand

import robot


class ToggleFieldOrientationCommand(InstantCommand):

    def __init__(self):
        super().__init__('Toggle Field Orientation')

        self.requires(robot.drivetrain)


    def initialize(self):
        robot.drivetrain.isFieldOriented = not robot.drivetrain.isFieldOriented
            
