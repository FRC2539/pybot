from wpilib.command import Command

import robot

class AutoSetWheelCommand(Command):
    def __init__(self):
        super().__init__('Auto Spin Wheel')

    def initialize(self):
        robot.colorwheel.autoSpinWheel() # Don't pass an argument, as the default value is the right value (or should be!)