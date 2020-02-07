from wpilib.command import Command

import robot

class IntakeCommand(Command):

    def __init__(self, speed=1):
        super().__init__('Intake')

        self.requires(robot.intake)
        self.speed = speed

    def initialize(self):
        robot.intake.intake(self.speed)
        print('\n\n\n\n RUNNING INTAKE\n\n\n\n\n')

    def end(self):
        print('\n\n\n\n\n\n STOPPING INTAKE \n\n\n\n')
        robot.intake.stop()
