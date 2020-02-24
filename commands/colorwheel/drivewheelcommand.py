from wpilib.command import Command

import robot


class DriveWheelCommand(Command):

    def __init__(self):
        super().__init__('Drive Wheel')

        self.requires(robot.colorwheel)

    def initialize(self):
        robot.colorwheel.spinClockwise()

    def end(self):
        robot.colorwheel.stop()
