from wpilib.command import Command

import robot


class RevolverGoBackCommand(Command):

    def __init__(self):
        super().__init__('Revolver Go Back')

        self.requires(robot.revolver)


    def initialize(self):
        robot.revolver.setVariableSpeed(-.7)
        pass

    def execute(self):
        robot.revolver.setVariableSpeed(-.7)
        pass

    def end(self):
        robot.revolver.stopRevolver()
        pass
