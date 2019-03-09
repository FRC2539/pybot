from wpilib.command.command import Command

import robot

class SuperStructureGoToLevelCommand(Command):

    def __init__(self, level):
        super().__init__('SuperStructure Go To Level')

        self.requires(robot.arm)
        self.requires(robot.elevator)

        self.level = level


    def initialize(self):
        self.armUOD = ''
        self.eleUOD = ''
        self.armDone = False
        self.eleDone = False

        armPos = robot.arm.getPosition()
        elePos = robot.elevator.getPosition()

        if robot.arm.levels[self.level] <= armPos + 1.0 and robot.arm.levels[self.level] >= armPos - 1.0:
            self.armUOD = ''
        elif robot.arm.levels[self.level] > armPos:
            self.armUOD = 'up'
        elif robot.arm.levels[self.level] < armPos:
            self.armUOD = 'down'

        if robot.elevator.levels[self.level] <= elePos + 1.0 and robot.elevator.levels[self.level] >= elePos - 1.0:
            self.eleUOD = ''
        elif robot.elevator.levels[self.level] > elePos:
            self.eleUOD = 'up'
        elif robot.elevator.levels[self.level] < elePos:
            self.eleUOD = 'down'


    def execute(self):
        self.armDone = robot.arm.goToLevel(self.level, self.armUOD)
        self.eleDone = robot.elevator.goToLevel(self.level, self.eleUOD)


    def isFinished(self):
        return self.armDone and self.eleDone


    def end(self):
        robot.elevator.stop()
        robot.arm.stop()
