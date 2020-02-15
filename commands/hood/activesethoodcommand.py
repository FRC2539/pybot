from wpilib.command import Command

import robot

class ActiveSetHoodCommand(Command):

    def __init__(self, angle):
        super().__init__('Active Set Hood')

        self.requires(robot.hood)
        self.angle = angle

    def initialize(self):
        robot.hood.setShootAngle(self.angle)

    def end(self):
        robot.hood.stopHood()
