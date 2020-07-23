from wpilib.command import Command

from controller import logicalaxes

import robot

logicalaxes.registerAxis('speedControl')

class VariableSpeedCommand(Command):

    def __init__(self):
        super().__init__()

        self.requires(robot.revolver)

    def execute(self):
        robot.revolver.setVariableSpeed(logicalaxes.speedControl.get())

    def end(self):
        robot.revolver.stopRevolver()
