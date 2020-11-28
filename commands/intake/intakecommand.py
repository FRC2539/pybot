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
            print('LOWERED')
            robot.pneumatics.retractIntakeSolenoid()
            robot.intake.stopIntake()
        else:
            print('HIGH')
            robot.pneumatics.extendIntakeSolenoid()
            robot.intake.intakeBalls()
        
