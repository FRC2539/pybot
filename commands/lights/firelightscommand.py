from wpilib.command.command import Command

import robot

class FireLightsCommand(Command):

    def __init__(self):
        super().__init__('Fire Lights')

        self.requires(robot.lights)


    def initialize(self):
        robot.lights.fire()


    def end(self):
        robot.lights.off()
