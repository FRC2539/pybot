from wpilib.command import Command

import robot


class UpdateWheelAnglesCommand(Command):
    def __init__(self, name="Update Wheel Angles"):
        super().__init__(name)

    def initialize(self):
        robot.drivetrain.updateModuleAngles()
