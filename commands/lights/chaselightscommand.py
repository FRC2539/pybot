from wpilib.command.command import Command

import robot

class ChaseLightsCommand(Command):

    def __init__(self):
        super().__init__('Chase Lights')

        self.requires(robot.lights)


    def initialize(self):
        robot.lights.chase()


    def end(self):
        robot.lights.off()
