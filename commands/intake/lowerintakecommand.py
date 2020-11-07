from wpilib.command import InstantCommand

import robot

class LowerIntakeCommand(InstantCommand):

    def __init__(self):
        super().__init__('Lower Intake')

    def initialize(self):
        robot.pneumatics.extendIntakeSolenoid()
        
