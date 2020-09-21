from wpilib.command import InstantCommand

import robot

class DeployIntakeCommand(InstantCommand):

    def __init__(self):
        super().__init__('Deploy Intake')
        
        self.requires(robot.intake)

    def initialize(self):
        robot.intake.stopIntake()

        if robot.pneumatics.isIntakeLowered():
            robot.pneumatics.retractIntakeSolenoid()
            robot.intake.stopIntake()
        else:
            robot.pneumatics.extendIntakeSolenoid()
            robot.intake.intakeBalls()
