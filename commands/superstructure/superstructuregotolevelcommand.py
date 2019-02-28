from wpilib.command.command import Command

import robot

class SuperStructureGoToLevelCommand(Command):

    def __init__(self, level):
        super().__init__('SuperStructure Go To Level')

        self.requires(robot.arm)
        self.requires(robot.elevator)

        self.level = level


    def initialize(self):

        self.armDone = 2
        self.eleDone = 2
        self.done = False


        self.armStart = robot.arm.getPosition()
        self.eleStart = robot.elevator.getPosition()

        print('Arm at ' + str(robot.arm.getPosition()))
        print('elevator at ' + str(robot.elevator.getPosition()))
        print('Going to ' + str(self.level))

        # 0 = Up, 1 = Down

        if robot.arm.levels[self.level] > self.armStart:
            print('arm start ' + str(self.armStart))
            self.armUOD = 0
        else:
            self.armUOD = 1

        if robot.elevator.levels[self.level] > self.eleStart:
            self.eleUOD = 0
        else:
            self.eleUOD = 1

        robot.arm.goToLevel(self.level)
        print('Moving arm')
        robot.elevator.goToLevel(self.level)
        print('Moving elevator')


    def execute(self):
        if (float(robot.arm.getPosition()) >= robot.arm.levels[self.level] and self.armUOD == 0) or (float(robot.arm.getPosition()) <= float(robot.arm.levels[self.level]) and self.armUOD == 1):
            robot.arm.stop()
            print('arm goal ' + str(robot.arm.levels[self.level]) + ' arm UOD ' + str(self.armUOD))
            self.armDone = 1

        if (float(robot.elevator.getPosition()) >= float(robot.elevator.levels[self.level]) and self.eleUOD == 0) or (float(robot.elevator.getPosition()) <= robot.elevator.levels[self.level] and self.eleUOD == 1):
            robot.elevator.stop()
            print('ele goal ' + str(robot.elevator.levels[self.level]) + ' ele UOD ' + str(self.eleUOD))
            self.eleDone = 1

        if self.eleDone == 1 and self.armDone == 1:
            print('done')
            self.done = True

        robot.arm.goToLevel(self.level)
        robot.elevator.goToLevel(self.level)


    def isFinished(self):
        return self.done


    def end(self):
        self.armDone = 2
        self.eleDone = 2
        self.done = False

        print('ended')

        robot.elevator.stop()
        robot.arm.stop()
