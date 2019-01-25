from wpilib.command.command import Command

import robot

class OrangeLightsCommand(Command):

    def __init__(self):
        super().__init__('Orange Lights')

        self.requires(robot.lights)


    def initialize(self):
        robot.lights.solidOrange()

    def end(self):
        robot.lights.off()


