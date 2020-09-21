from wpilib.command import Command

import robot

class EnsureEmptinessCommand(Command):

    def __init__(self):
        super().__init__('Ensure Emptiness')

        self.requires(robot.revolver)

    def initialize(self):
        robot.pneumatics.extendIntakeSolenoid()
        if robot.revolver.isEmpty():
            robot.revolver.disableRampRate()
            robot.revolver.stopRevolver()
        else:
            robot.revolver.enableRampRate()
            robot.revolver.setVariableSpeed(-0.6)
    
    def execute(self):
        if robot.revolver.isEmpty():
            robot.revolver.disableRampRate()
            robot.revolver.stopRevolver()
        else:
            robot.revolver.enableRampRate()
            robot.revolver.setVariableSpeed(-0.6)
            
    def end(self):
        robot.intake.stopIntake()
        robot.pneumatics.retractIntakeSolenoid()
        robot.revolver.enableRampRate()
        robot.revolver.stopRevolver()
