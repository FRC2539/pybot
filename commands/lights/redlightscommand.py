from wpilib.command.command import Command

import robot

class RedLightsCommand(Command):

    def __init__(self):
        super().__init__('Red Lights')

        self.requires(robot.lights)


    def initialize(self):
        robot.lights.solidRed()
