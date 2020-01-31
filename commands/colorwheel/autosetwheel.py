from wpilib.command import Command

import robot

class AutoSetWheelCommand(Command):
    def __init__(self):
        super().__init__('Auto Set Wheel')

        self.colors = ['y', 'r', 'g', 'b']

        self.direction = 1 # Clockwise
        self.distance = 0 # color spaces away

        self.colorDistance = 37.56 # 11.8", 37.56 rotations (30:1 + 3" diameter)

    def initialize(self):
        self.myColor = robot.colorwheel.getColor() # Make sure this provides the correct value, not an assumption
        self.desiredColor = 'r' # Make this come from FMS later. NOTE: If not a string, simply use a dictionary instead.

        self.distance = abs(self.colors[self.myColor] - self.colors[self.desiredColor])

        # Forward?
        if self.colors[self.myColor] < self.colors[self.desiredColor]:
            self.direction = 1

        elif self.colors[self.myColor] > self.colors[self.desiredColor]:
            self.direction = -1

        else:
            robot.colorwheel.spinToSensor()

        self.wheelactions.autoSpinWheel(self.colorDistance * self.colorDistance * self.direction)
