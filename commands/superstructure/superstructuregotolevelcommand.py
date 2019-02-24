from wpilib.command.command import Command

import robot

class SuperStructureGoToLevelCommand(Command):

    def __init__(self, level):
        super().__init__('SuperStructure Go To Level')

        self.requires(robot.arm)
        self.requires(robot.elevator)

        self.level = level

    def initialize(self):
        self.eleTarget = robot.elevator.goToLevel(self.level)
        self.armTarget = robot.arm.goToLevel(self.level)


    def execute(self):
        pass

    def isFinished(self):
        if abs(robot.arm.getPosition() - self.armTarget) < 5 and abs(robot.elevator.getPosition() - self.eleTarget) < 5:
            return 1

    def end(self):
        robot.elevator.stop()
        robot.arm.stop()
