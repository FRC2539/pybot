from wpilib.command import Command

import robot


class DetectAndQueueCommand(Command):

    def __init__(self):
        super().__init__('Detect And Queue')

        self.requires(robot.ballsystem)
        self.requires(robot.intake)

    def initialize(self):
        robot.intake.stop()
        robot.ballsystem.stopAll()

    def execute(self):
        if robot.ballsystem.needsToQueue() and (not robot.ballsystem.isUpperBallPrimed()):
            robot.ballsystem.runAllSlow()

        else:
            robot.ballsystem.stopAll()

        if not robot.ballsystem.isUpperBallPrimed():
            robot.intake.intake(0.35)

        else:
            robot.intake.stop()

    def end(self):
        robot.ballsystem.stopAll()
        robot.intake.stop()
