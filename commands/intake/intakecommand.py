from wpilib.command import Command

import robot

class IntakeCommand(Command):

    def __init__(self, speed=1):
        super().__init__('Intake')

        self.requires(robot.intake)
        self.speed = speed

    def initialize(self):
        robot.intake.intake(self.speed)

    def execute(self):
        robot.intake.sensorCount()

    def end(self):
        robot.intake.stop()
