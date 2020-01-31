from wpilib.command import Command

import robot

class IntakeCommand(Command):
    def __init__(self):
        super().__init__('Intake')

        self.requires(robot.intake)

    def initialize(self):
        robot.intake.intake()

    def execute(self):
        robot.intake.monitorIntake()

    def end(self):
        robot.intake.maintainBalls() # Or maybe just stop it...