from wpilib.command.command import Command

import robot

class SuperStructureGoToLevelCommand(Command):

    def __init__(self, level):
        super().__init__('SuperStructure Go To Level')

        self.requires(robot.arm)
        self.requires(robot.elevator)

        self.level = level


    def initialize(self):
        robot.elevator.goToLevel(self.level)
        robot.arm.goToLevel(self.level)


    def execute(self):
        pass


    def end(self):
        pass
