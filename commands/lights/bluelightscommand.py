from wpilib.command.command import Command

import robot

class BlueLightsCommand(Command):

    def __init__(self):
        super().__init__('Blue Lights')

        self.requires(robot.lights)


    def initialize(self):
        robot.lights.solidBlue()
