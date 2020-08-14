from wpilib.command import Command

import robot

import math


class AdvancedMoveCommand(Command):

    def __init__(self):
        super().__init__('Advanced Move')

        self.requires(robot.revolver)

        self.nextTarget = 0

        self.smallJump = True
        self.dirMod = 1
        self.pattern = [True, True, False]
        self.count = 0

    def initialize(self):
        # Set to a position in the list

        start = robot.revolver.getAbsolute()

        diffs = {}

        id_ = 0
        for x in robot.revolver.holeLocations:
            diffs[x - start] = id_
            id_ += 1

        self.nextTarget = robot.revolver.holeLocations[diffs[min(diffs.keys())]]

        robot.revolver.setPosition(self.nextTarget)


    def execute(self):
        print('a ' + str(robot.revolver.getAbsolute()))
        print('nt ' + str(self.nextTarget))

        print('ap ' + str(robot.revolver.atPosition(self.nextTarget)))

        self.smallJump = self.pattern[self.count]

        if robot.revolver.atPosition(self.nextTarget):
            if self.smallJump:
                self.nextTarget += 0.1 * self.dirMod
                self.dirMod *= -1
                robot.revolver.setPosition(self.nextTarget)
                print('set')
            else:
                self.nextTarget += 0.2
                robot.revolver.setPosition(self.nextTarget)

            if self.count == 2:
                self.count = 0
            else:
                self.count += 1

            if self.nextTarget == 1:
                self.nextTarget = 0

    def end(self):
        robot.revolver.stopRevolver()
