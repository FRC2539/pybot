from wpilib.command import Command

import robot


class RunUntilEmptyCommand(Command):

    def __init__(self, ballCount):
        super().__init__('Run Until Empty')

        self.requires(robot.ballsystem)

        self.ballCount = ballCount
        self.primed = False

    def initialize(self):
        if robot.ballsystem.isUpperBallPrimed():
            self.primed = True

        robot.ballsystem.runAll()

    def execute(self):
        if self.primed and not robot.ballsystem.isUpperBallPrimed(): # if there was a ball there and its not, it's shot.
            self.ballCount -= 1
            self.primed = False

        if robot.ballsystem.isUpperBallPrimed(): # saw it, when it does not see it next, assumes it has been shot.
            self.primed = True

    def isFinished(self):
        return (self.ballCount <= 0)

    def end(self):
        robot.ballsystem.stopAll()
