from wpilib.command import Command

import robot

class ReverseWheelCommand(Command):

    def __init__(self):
        super().__init__('Reverse Wheel')

        self.requires(robot.colorwheel)

    def initialize(self):
        robot.colorwheel.spinCClockwise()

    def end(self):
        robot.colorwheel.stop()
