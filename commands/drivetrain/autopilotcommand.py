from wpilib.command import Command

from controller import logicalaxes

import robot

logicalaxes.registerAxis('driveY')
logicalaxes.registerAxis('driveRotate')

class AutoPilotCommand(Command):

    def __init__(self):
        super().__init__('Auto Pilot')

        self.requires(robot.drivetrain)

        robot.drivetrain.resetGyro()

        self.engaged = False
    
    def initialize(self):
        self.engaged = False

    def execute(self):
        self.currentHeading = robot.drivetrain.getAngle()
                
        y = logicalaxes.driveY.get() * 0.8
        
        if not self.engaged: # Allows it to find it only once.
            self.engaged = (abs(self.currentHeading - 180) <= 30) or (not 330 >= self.currentHeading >= 30) # 15 degrees of freedom on both sides. 
            rotate = logicalaxes.driveRotate.get() * 0.45
        else:
            
            if not 90 < self.currentHeading < 270:
                rotate = robot.drivetrain.getAngleTo(0) / 90
            else:
                rotate = robot.drivetrain.getAngleTo(180) / 90
        
        print('rrrrrrrr ' +  str(rotate))
        
        robot.drivetrain.move(
            0,
            y,
            rotate
        )

    def end(self):
        robot.drivetrain.stop()
