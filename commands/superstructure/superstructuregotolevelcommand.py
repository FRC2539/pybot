from wpilib.command.command import Command

import robot

class SuperStructureGoToLevelCommand(Command):

    def __init__(self, level):
        super().__init__('SuperStructure Go To Level')

        self.requires(robot.arm)
        self.requires(robot.elevator)

        self.level = level


    def initialize(self):
        self.eleDone = False
        self.armDone = False
        self.armUOD = ''
        self.eleUOD = ''

        if robot.arm.levels[self.level] > robot.arm.getPosition():
            self.armUOD = 'up'
        else:
            self.armUOD = 'down'

        if robot.elevator.levels[self.level] > robot.elevator.getPosition():
            self.eleUOD = 'up'
        else:
            self.eleUOD = 'down'


    def isFinished(self):
        if robot.arm.goToLevel(self.level, self.armUOD):
            robot.arm.stop()
            self.armDone = True
        if robot.elevator.goToLevel(self.level, self.eleUOD):
            robot.elevator.stop()
            self.eleDone = True

        if self.eleDone and self.armDone:
            return True

    def end(self):
        robot.elevator.stop()
        robot.arm.stop()
