from wpilib.command import Command

import robot

class IntakeCommand(Command):

    def __init__(self):
        super().__init__('Intake')

        self.requires(robot.intake)

    def initialize(self):
        robot.intake.intakeBalls()

    def end(self):
        robot.intake.stopIntake()
