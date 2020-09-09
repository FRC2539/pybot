from wpilib.command import Command

import robot

class VariableSpeedCommand(Command):

    def __init__(self, speed):
        super().__init__()

        self.requires(robot.revolver)

        self.speed = speed

    def initialize(self):
        robot.revolver.setVariableSpeed(self.speed)

    def execute(self):
        robot.revolver.setVariableSpeed(self.speed)

    def end(self):
        robot.revolver.stopRevolver()
