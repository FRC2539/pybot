from wpilib.command import Command

import robot

class IntakeCommand(Command):

    def __init__(self):
        super().__init__('Intake')

        self.requires(robot.intake)


    def initialize(self):
        robot.intake.intake()
        print('\n\n\n\n RUNNING INTAKE\n\n\n\n\n')

    def execute(self):
        pass


    def end(self):
        print('\n\n\n\n\n\n STOPPING INTAKE \n\n\n\n')
        robot.intake.stop()
