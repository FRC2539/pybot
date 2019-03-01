from wpilib.command.command import Command

import robot

class VisionBasedLightsCommand(Command):

    def __init__(self):
        super().__init__('Vision Based Lights')

        self.requires(robot.lights)


    def execute(self):
        self.val, self.distance = robot.lights.visionBasedLights()
        self.ratio = self.distance * 0.1

        if self.val == -10:
            robot.lights.solidRed()

        elif self.val <= self.ratio:
            robot.lights.solidBlue()

        elif self.val > self.ratio:
            robot.lights.solidPurple()

    def end(self):
        robot.lights.off()
