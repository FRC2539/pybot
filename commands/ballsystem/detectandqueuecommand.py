from wpilib.command import Command

import robot


class DetectAndQueueCommand(Command):

    def __init__(self):
        super().__init__('Detect And Queue')

        self.requires(robot.ballsystem)

    def initialize(self):
        robot.ballsystem.stopAll()

    def execute(self):
        if robot.ballsystem.needsToQueue() and (not robot.ballsystem.isUpperBallPrimed()):
            robot.ballsystem.runAllSlow()

        else:
            robot.ballsystem.stopAll()

    def end(self):
        robot.ballsystem.stopAll()
