from wpilib.command.instantcommand import InstantCommand

import robot

class LightsOffCommand(InstantCommand):

    def __init__(self):
        super().__init__('Lights Off')

        self.requires(robot.lights)


    def initialize(self):
        robot.lights.off()


