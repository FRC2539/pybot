from wpilib.command import Command

from wpilib import Timer

import robot


class RunUntilEmptyCommand(Command):

    def __init__(self, ballCount, desiredRPM=4200, tol=200):
        super().__init__('Run Until Empty')

        self.requires(robot.ballsystem)

        self.rpm = desiredRPM
        self.tol = tol

        self.timer = Timer()

        self.ballCount = ballCount
        self.primed = False

    def initialize(self):
        self.timer.start()
        if robot.ballsystem.isUpperBallPrimed():
            self.primed = True

        if robot.shooter.getRPM() >= (self.rpm - self.tol):
            robot.ballsystem.runVerticalConveyor()
            robot.ballsystem.reverseLowerConveyorSlow()

            if self.timer.hasElapsed(1):
                robot.ballsystem.safeRunAll()

    def execute(self):

        if self.primed and not robot.ballsystem.isUpperBallPrimed(): # if there was a ball there and its not, it's shot.
            self.ballCount -= 1
            self.primed = False

        if robot.ballsystem.isUpperBallPrimed(): # saw it, when it does not see it next, assumes it has been shot.
            self.primed = True

        if robot.shooter.getRPM() >= (self.rpm - self.tol):
            print('running vertical only!\n')
            robot.ballsystem.safeRunVertical()
            if self.timer.hasElapsed(1):
                print('RUNNING ALL BS!\n')
                robot.ballsystem.runAll()
                self.timer.stop()

        else:
            robot.ballsystem.stopAll()

        print('ball count ' + str(self.ballCount))

    def isFinished(self):
        return (self.ballCount <= 0)

    def end(self):
        self.timer.reset()
        robot.ballsystem.stopAll()
