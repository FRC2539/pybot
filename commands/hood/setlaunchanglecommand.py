from wpilib.command import Command

import robot

class SetLaunchAngleCommand(Command):

    def __init__(self, val):
        super().__init__('Set Launch Angle')

        self.requires(robot.hood)
        self.angle = val


    def initialize(self):
        pass


    def execute(self):
        robot.hood.setShootAngle(self.angle)


    def end(self):
        robot.hood.stopHood()
