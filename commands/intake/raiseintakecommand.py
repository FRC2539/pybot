from wpilib.command import InstantCommand

import robot

class RaiseIntakeCommand(InstantCommand):

    def __init__(self):
        super().__init__('Raise Intake')

        self.requires(robot.intake)

    def initialize(self):
        robot.intake.stopIntake()
        robot.pneumatics.retractIntakeSolenoid()
