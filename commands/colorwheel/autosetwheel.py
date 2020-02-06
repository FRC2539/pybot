from wpilib.command import Command

import robot

class AutoSetWheelCommand(Command):
    def __init__(self):
        super().__init__('Auto Set Wheel')

        self.requires(robot.colorwheel)

        self.colors = ['y', 'r', 'g', 'b']

        self.direction = 1 # Clockwise
        self.distance = 0 # color spaces away

        self.colorDistance = 37.56 # 11.8", 37.56 rotations (30:1 + 3" diameter) per color section

    def initialize(self):
        self.myColor = 'y'#robot.colorwheel.getColor() # Make sure this provides the correct value, not an assumption
        self.desiredColor = 'r' # Make this come from FMS later. NOTE: If not a string, simply use a dictionary instead.

        self.distance = abs(self.colors.index(self.myColor) - self.colors.index(self.desiredColor))

        # Forward?
        if self.colors.index(self.myColor) < self.colors.index(self.desiredColor):
            self.direction = 1
            self.distance -= 2.2 #  Adjust to get to sensor (might need to add)

        elif self.colors.index(self.myColor) > self.colors.index(self.desiredColor):
            self.direction = -1
            self.distance += 2.2 # Adjust to get to sensor (might need to subtract)

        else:
            robot.colorwheel.spinToSensor(75.12) # 37.56 * 2

        print('self.distance ' + str(self.distance))


        robot.colorwheel.autoSpinWheel(self.colorDistance * self.colorDistance * self.direction)
