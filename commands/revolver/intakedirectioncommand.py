from wpilib.command import Command

import robot

class IntakeDirectionCommand(Command):

    def __init__(self):
        super().__init__('Intake Direction')

        self.requires(robot.revolver)

    def initialize(self):
        robot.revolver.setVariableSpeed(-0.15)

    def end(self):
        robot.revolver.stopRevolver()
