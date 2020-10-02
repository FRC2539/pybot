from wpilib.command import Command

import robot

class KickCommand(Command):

    def __init__(self):
        super().__init__('Kick Command')

        self.requires(robot.intake)

    def initialize(self):
        robot.intake.outakeBalls()

    def end(self):
        robot.intake.stopIntake()
