from wpilib.command import Command

import robot

class EnsureEmptinessCommand(Command):

    def __init__(self):
        super().__init__('Ensure Emptiness')

        self.requires(robot.revolver)

        self.there = False

    def initialize(self):
        if robot.revolver.isFrontEmpty() and robot.revolver.atHole() and not self.there:
            robot.revolver.stopRevolver()
            self.there = True

        elif robot.revolver.isFrontEmpty() and not self.there:
            robot.revolver.stopRevolver()

        else:
            self.there = False
            robot.revolver.setVariableSpeed(0.5)

    def execute(self):
        print('hole ' + str(robot.revolver.atHole()))
        print('empty ' + str(robot.revolver.isFrontEmpty()))

        if robot.revolver.isFrontEmpty() and robot.revolver.atHole() and not self.there:
            robot.revolver.stopRevolver()
            self.there = True

        elif robot.revolver.isFrontEmpty() and not self.there:
            robot.revolver.stopRevolver()

        else:
            self.there = False
            robot.revolver.setVariableSpeed(0.5)

    def end(self):
        robot.revolver.stopRevolver()
        robot.balllauncher.stopLauncher()
