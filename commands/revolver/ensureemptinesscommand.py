from wpilib.command import Command

import robot

class EnsureEmptinessCommand(Command):

    def __init__(self):
        super().__init__('Ensure Emptiness')

        self.requires(robot.revolver)

    def initialize(self):
        if robot.revolver.isFrontEmpty():
            robot.revolver.stopRevolver()
        else:
            robot.revolver.setVariableSpeed(-0.35)

    def execute(self):
        if robot.revolver.isFrontEmpty():
            robot.revolver.stopRevolver()

        else:
            robot.revolver.setVariableSpeed(-0.35)

    def end(self):
        robot.revolver.stopRevolver()
