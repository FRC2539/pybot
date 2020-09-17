from wpilib.command import Command

import robot

class EnsureEmptinessCommand(Command):

    def __init__(self):
        super().__init__('Ensure Emptiness')

        self.requires(robot.revolver)

    def initialize(self):
        if robot.revolver.isEmpty():
            robot.revolver.disableRampRate()
            robot.revolver.stopRevolver()
        else:
            robot.revolver.enableRampRate()
            robot.revolver.setVariableSpeed(0.5)
    
    def execute(self):
        print('signal one ' + str(robot.revolver.getZoneOne()))
        if robot.revolver.isEmpty():
            robot.revolver.disableRampRate()
            robot.revolver.stopRevolver()
        else:
            robot.revolver.enableRampRate()
            robot.revolver.setVariableSpeed(0.5)
            
    def end(self):
        robot.revolver.enableRampRate()
        robot.revolver.stopRevolver()
