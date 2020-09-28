from wpilib.command import InstantCommand

from subsystems.cougarsystem import *

import robot

class IntakeCommand(InstantCommand):

    def __init__(self):
        super().__init__('Intake')

        self.requires(robot.intake)

    def initialize(self):        
        if not robot.intake.intaking:
            if not robot.pneumatics.isIntakeLowered():
                robot.pneumatics.extendIntakeSolenoid()
            
            robot.intake.intakeBalls()
        
        else:
            robot.intake.stopIntake()
