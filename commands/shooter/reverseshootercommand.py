from wpilib.command import Command

import robot

class ReverseShooterCommand(Command):

    def __init__(self):
        super().__init__('Reverse Shooter')

        self.requires(robot.shooter)
        self.requires(robot.ballsystem)

    def initialize(self):
        robot.ballsystem.reverseAll()
        robot.shooter.reverse()

    def end(self):
        robot.ballsystem.stopAll()
        robot.shooter.stop()
