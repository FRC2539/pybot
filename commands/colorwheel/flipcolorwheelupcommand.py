from wpilib.command import InstantCommand

import robot

class FlipColorwheelUpCommand(InstantCommand):

    def __init__(self):
        super().__init__('Flip Colorwheel Up')

        self.requires(robot.colorwheel)

    def initialize(self):
        robot.colorwheel.flipColorWheelUp()
