from wpilib.command import Command

import robot


class RunUntilEmptyCommand(Command):

    def __init__(self, ballCount):
        super().__init__('Run Until Empty')

        self.requires(robot.ballsystem)
        self.requires(robot.shooter)

        self.ballCount = ballCount

    def initialize(self):
      #  robot.shooter.setRPM(4200) # sets if not already set
        robot.shooter.setGoalNetworkTables()

        robot.ballsystem.runAll()

    def execute(self):
        self.ballCount = robot.ballsystem.monitorBalls(self.ballCount)

        robot.shooter.updateNetworkTables()

    def isFinished(self):
        return (self.ballCount == 0)

    def end(self):
        robot.shooter.stop()
        robot.ballsystem.stopAll()
