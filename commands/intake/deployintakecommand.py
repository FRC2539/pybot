from wpilib.command import InstantCommand

import robot

class DeployIntakeCommand(InstantCommand):

    def __init__(self):
        super().__init__('Deploy Intake')

    def initialize(self):
        robot.intake.stopIntake()

        if robot.pneumatics.isIntakeLowered():
            robot.pneumatics.retractIntakeSolenoid()
        else:
            robot.pneumatics.extendIntakeSolenoid()
