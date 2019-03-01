from wpilib.command.command import Command

import robot

class VisionBasedLightsCommand(Command):

    def __init__(self):
        super().__init__('Vision Based Lights')

        self.requires(robot.lights)


    def execute(self):
        self.val = robot.lights.visionBasedLights()

        if self.val == 20:
            robot.lights.solidRed()

        elif self.val < 3:
            robot.lights.solidBlue()

        elif self.val >= 4 and self.val <= 15:
            robot.lights.solidPurple()

    def end(self):
        robot.lights.off()
