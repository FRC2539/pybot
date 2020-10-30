from wpilib.command import InstantCommand

import robot

class CycleSongLeft(InstantCommand):
    
    def __init__(self):
        super().__init__('Music')
        
        self.requires(robot.drivetrain)
        
    def initialize(self):
        robot.drivetrain.stop()
        
        try:
            robot.drivetrain.stopM()
            robot.drivetrain.cycleLeft()
            
        except(AttributeError):
            print('Wrong drivebase my friend . . . ?')
