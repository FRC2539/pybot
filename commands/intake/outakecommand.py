from wpilib.command import Command

import robot

class OutakeCommand(Command):

    def __init__(self):
        super().__init__('Outake')

        self.requires(robot.intake)

    def initialize(self):
        robot.intake.outakeBalls()

    def end(self):
        robot.intake.stopIntake()
