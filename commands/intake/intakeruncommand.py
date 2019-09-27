from wpilib.command.command import Command

import robot

class IntakerunCommand(Command):

    def __init__(self):
        super().__init__('Intakerun',2)

        self.requires(robot.intake)


    def initialize(self):

        robot.intake.intake()


    def end(self):

        robot.intake.stop()
