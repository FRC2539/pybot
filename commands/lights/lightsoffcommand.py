from wpilib.command.command import Command

import robot

class LightsOffCommand(Command):

    def __init__(self):
        super().__init__('Lights Off')

        self.requires(robot.lights)


    def initialize(self):
        robot.lights.off()


