from wpilib.command import InstantCommand

import robot

class CycleSongRight(InstantCommand):
    
    def __init__(self):
        super().__init__('Music')
        
        self.requires(robot.drivetrain)
        
    def initialize(self):
        robot.drivetrain.stop()
        
        try:
            robot.drivetrain.stopM()
            robot.drivetrain.cycleRight()
            
        except(AttributeError):
            print('Wrong drivebase my friend . . . ?')
