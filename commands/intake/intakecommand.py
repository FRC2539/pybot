from wpilib.command import InstantCommand

from subsystems.cougarsystem import *

import robot

class IntakeCommand(InstantCommand):

    def __init__(self):
        super().__init__('Intake')

        self.requires(robot.intake)

    def initialize(self):        
        robot.intake.stopIntake()

        if robot.pneumatics.isIntakeLowered():
            robot.pneumatics.retractIntakeSolenoid()
            robot.intake.stopIntake()
        else:
            robot.pneumatics.extendIntakeSolenoid()
            robot.intake.intakeBalls()

