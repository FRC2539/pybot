from wpilib.command import Command

import robot

class StopShooterCommand(Command):

    def __init__(self):
        super().__init__('Stop Shooter')

        self.requires(robot.shooter)

    def initialize(self):
        robot.shooter.stop()

