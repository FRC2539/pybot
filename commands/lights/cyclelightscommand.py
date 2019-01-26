from wpilib.command.instantcommand import InstantCommand

import robot

class CycleLightsCommand(InstantCommand):

    def __init__(self):
        super().__init__('Cycle Lights')

        self.requires(robot.lights)
        self.colorcycle = -0.99

    def initialize(self):
        self.colorcycle += 0.02
        if self.colorcycle > 0.99:
            self.colorcycle = -0.99
        print(str(self.colorcycle))
        robot.lights.setSpecific(self.colorcycle)
