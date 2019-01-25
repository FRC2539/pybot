from wpilib.command.command import Command

import robot
import time

class TeamColorLightsCommand(Command):

    def __init__(self):
        super().__init__('Team Color Lights')

        self.requires(robot.lights)
        self.colorvalue = 0

    def execute(self):

        if self.colorvalue <= 1:
            robot.lights.solidOrange()
            self.colorvalue += 1

        elif self.colorvalue <= 2:
            robot.lights.solidWhite()
            self.colorvalue += 1

        elif self.colorvalue <= 3:
            robot.lights.off()
            self.colorvalue = 0

        time.sleep(1.2)

    def end(self):
        robot.lights.off()
