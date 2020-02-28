from wpilib.command import Command

import robot

class AutoSpinWheelCommand(Command):
    def __init__(self):
        super().__init__('Auto Spin Wheel')

        self.requires(robot.colorwheel)

    def initialize(self):
        robot.colorwheel.autoSpinWheel() # Don't pass an argument, as the default value is the right value (or should be!)

    def execute(self):
        print('cw ' + str(robot.colorwheel.getEncPosition()))

    def end(self):
        robot.colorwheel.stop()
