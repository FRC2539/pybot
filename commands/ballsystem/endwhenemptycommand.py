from wpilib.command import Command

import robot


class EndWhenEmptyCommand(Command):

    def __init__(self, ballCount):
        super().__init__('End When Empty')

        self.requires(robot.ballsystem)
        self.balls = ballCount
        self.primed = False

    def isFinished(self):
        if self.primed and not robot.ballsystem.isUpperBallPrimed(): # if there was a ball there and its not, it's shot.
            self.balls -= 1
            self.primed = False

        if robot.ballsystem.isUpperBallPrimed(): # saw it, when it does not see it next, assumes it has been shot.
            self.primed = True

        return (self.balls == 0)

    def end(self):
        robot.ballsystem.stopAll()
