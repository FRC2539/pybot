from wpilib.command import Command

import robot


class ActualRevolverShakeCommand(Command):

    def __init__(self):
        super().__init__('Actual Revolver Shake')

        self.requires(robot.revolver)
        self.iterations = 0
        
    def initialize(self):
        self.iterations = 0
        self.maxIter = 32
        robot.revolver.setVariableSpeed(.7)
        robot.revolver.motor.setClosedLoopRampRate(0.1)
        robot.revolver.motor.setOpenLoopRampRate(0.1)

    def execute(self):
        print("the command is running and " + str(self.iterations >= self.maxIter/2))
        self.iterations += 1
        if self.iterations == self.maxIter/2:
            robot.revolver.setVariableSpeed(-.5)
        elif self.iterations >= self.maxIter:
            robot.revolver.setVariableSpeed(.5)
            self.iterations = 0

    def end(self):
        robot.revolver.stopRevolver()
        robot.revolver.motor.setClosedLoopRampRate(2)
        robot.revolver.motor.setOpenLoopRampRate(2)
        pass
