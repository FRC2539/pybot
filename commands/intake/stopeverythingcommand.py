from wpilib.command import InstantCommand

import robot

class StopEverythingCommand(InstantCommand):

    def __init__(self):
        super().__init__('Stop Everything')

        self.requires(robot.intake)
        self.requires(robot.shooter)
        self.requires(robot.ballsystem)

    def initialize(self):
        robot.ballsystem.stopAll()
        robot.intake.stop()
        robot.shooter.stop()

    def end(self):
        pass
