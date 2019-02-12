from wpilib.command.command import Command

import robot

class ArmGoToLevelCommand(Command):

    def __init__(self, level):
        super().__init__('Arm Go To Level')

        self.requires(robot.elevator)
        self.level = level


    def initialize(self):
        robot.arm.goToLevel(self.level)


    def execute(self):
        pass


    def end(self):
        pass
