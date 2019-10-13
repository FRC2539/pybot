from wpilib.command.command import Command

import robot

class StopIntakeCommand(Command):

    def __init__(self):
        super().__init__('Stop Intake')

        self.requires(robot.pneumatics)


    def initialize(self):
        robot.pneumatics.stopIntake()
