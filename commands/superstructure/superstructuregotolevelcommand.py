from wpilib.command.command import Command

import robot

class SuperStructureGoToLevelCommand(Command):

    def __init__(self, level):
        super().__init__('SuperStructure Go To Level')

        self.requires(robot.arm)
        self.requires(robot.elevator)

        self.level = level

        self.armTarget = robot.arm.levels[self.level]
        self.eleTarget = robot.elevator.levels[self.level]

        print("at: "+str(self.armTarget))
        print("et: "+str(self.eleTarget))


    def initialize(self):
        self.armUOD = ''
        self.eleUOD = ''
        self.armDone = False
        self.eleDone = False
        self.armPos = robot.arm.getPosition()
        self.elePos = robot.elevator.getPosition()

        if self.armTarget <= (self.armPos + 1.0) and self.armTarget >= (self.armPos - 1.0):
            self.armUOD = ''
        elif self.armTarget > self.armPos:
            self.armUOD = 'up'
        elif self.armTarget < self.armPos:
            self.armUOD = 'down'

        if self.eleTarget <= (self.elePos + 1.0) and self.eleTarget >= (self.elePos - 1.0):
            self.eleUOD = ''
        elif self.eleTarget > self.elePos:
            self.eleUOD = 'up'
        elif self.eleTarget < self.elePos:
            self.eleUOD = 'down'


    def execute(self):
        self.armPos = robot.arm.getPosition()
        self.elePos = robot.elevator.getPosition()

        print("armTarget: "+str(self.armTarget))


        if not self.armDone:
            if self.armUOD == 'up' and self.armPos < self.armTarget:
                robot.arm.up()

            elif self.armUOD == 'down' and self.armPos > self.armTarget:
                robot.arm.down()

            else:
                robot.arm.stop()
                self.armDone = True
                print("armDone: "+str(self.armPos))

        if not self.eleDone:
            if self.eleUOD == 'up' and self.elePos < self.eleTarget:
                robot.elevator.up()

            elif self.eleUOD == 'down' and self.elePos > self.eleTarget:
                robot.elevator.down()

            else:
                robot.elevator.stop()
                self.eleDone = True
                print("armDone: "+str(self.eleDone))


    def isFinished(self):
        return self.armDone and self.eleDone


    def end(self):
        robot.elevator.stop()
        robot.arm.stop()
