from wpilib.command import Command

from wpilib import Timer

import robot


class DetectAndQueueCommand(Command):

    def __init__(self):
        super().__init__('Detect And Queue')

        self.requires(robot.ballsystem)
        self.requires(robot.intake)

        self.t = Timer()

    def initialize(self):
        robot.intake.stop()
        robot.ballsystem.stopAll()

        self.waiting = False

    def execute(self):
        if robot.ballsystem.needsToQueue() and (not robot.ballsystem.isUpperBallPrimed()):
            robot.ballsystem.runAllSlow()
            self.waiting = False

        else:
            if robot.ballsystem.isUpperBallPrimed():
                if not self.waiting:
                    self.waiting = True
                    self.t.reset()
                    self.t.start()
                    robot.ballsystem.runVerticalSlow()

                if self.t.get() >= 0.1:
                    self.t.stop()
                    robot.ballsystem.stopAll()

            else:
                robot.ballsystem.stopAll()

        if not robot.ballsystem.isUpperBallPrimed():
            robot.intake.intake(0.35)

        else:
            robot.intake.stop()

    def end(self):
        robot.ballsystem.stopAll()
        robot.intake.stop()
