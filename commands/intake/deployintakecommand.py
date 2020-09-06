from wpilib.command import Command

import robot

class DeployIntakeCommand(Command):

    def __init__(self):
        super().__init__('Deploy Intake')

    def initialize(self):
        robot.pneumatics.extendIntakeSolenoid()

    def end(self):
        robot.pneumatics.retractIntakeSolenoid()
