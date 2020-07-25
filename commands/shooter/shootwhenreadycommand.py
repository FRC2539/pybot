from wpilib.command import Command

import robot

class ShootWhenReadyCommand(Command):

    def __init__(self, targetRPM):
        super().__init__('Shoot When Ready')

        self.requires(robot.shooter)
        self.requires(robot.balllauncher)

        self.targetRPM = targetRPM

    def initialize(self):
        robot.shooter.setRPM(self.targetRPM)

    def execute(self):
        if robot.shooter.getRPM() >= self.targetRPM:
            robot.balllauncher.launchBalls()

        else:
            robot.balllauncher.stopLauncher()

    def end(self):
        robot.shooter.stopShooter()
        robot.balllauncher.stopLauncher()
