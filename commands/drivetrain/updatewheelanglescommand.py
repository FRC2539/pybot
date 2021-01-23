from wpilib.command import InstantCommand

import robot

class UpdateWheelAnglesCommand(InstantCommand):
    
    def __init__(self, name="Update Wheel Angles"):
        super().__init__(name)
        
    def initialize(self):
        robot.drivetrain.updateModuleAngles()