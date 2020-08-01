from wpilib.command import Command

import robot

class hoodTestCommand(Command):

    def __init__(self):
        super().__init__('hood Test')

        self.requires(robot.hood)


    def initialize(self):
        pass


    def execute(self):
        robot.hood.setShootAngle(30)
        robot.hood.pEncoder()

    def end(self):
        pass
