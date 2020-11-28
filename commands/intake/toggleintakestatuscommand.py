from wpilib.command import InstantCommand

import robot

class ToggleIntakeStatusCommand(InstantCommand):

    def __init__(self):
        super().__init__('Toggle Intake Status')

        self.requires(robot.intake)

    def initialize(self):
        robot.pneumatics.extendIntakeSolenoid()


