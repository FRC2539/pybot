from wpilib.command import Command

import robot

class MusicCommand(Command):
    
    def __init__(self):
        super().__init__('Music')
        
        self.requires(robot.drivetrain)
        
    def initialize(self):
        robot.drivetrain.stop()
        
        try:
            robot.drivetrain.playM()
        except(AttributeError):
            print('Wrong drivebase my friend . . . ?')
            
    def end(self):
        
        try:
            robot.drivetrain.stopM()
        except(AttributeError):
            pass
