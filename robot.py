import wpilib
import magicbot
import ports

from components.drivebase.robotdrive import RobotDrive

from controller.logitechdualshock import LogitechDualshock
from . import logicalaxes

from ctre import WPI_TalonSRX

import shutil, sys

class CleanRobot(magicbot.MagicRobot):
    drivetrain: RobotDrive('tank') # creates a drivetrain object
    
    def createObjects(self):
        self.drivetrainMotors = [
                    WPI_TalonSRX(ports.DrivetrainPorts.FrontLeftMotor),
                    WPI_TalonSRX(ports.DrivetrainPorts.FrontRightMotor),
                    WPI_TalonSRX(ports.DrivetrainPorts.BackLeftMotor),
                    WPI_TalonSRX(ports.DrivetrainPorts.BackRightMotor)
                    ]
        ''' Create motors and stuff here (init)'''    
        
        self.controller = BuildLayout(0)
    
    def teleopInit(self):
        ''' Starts at the beginning of teleop (initialize) '''
        
    def teleopPeriodic(self):
        ''' Starts on each iteration of the control loop (execute) '''
    
    
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'deploy':
        shutil.rmtree('opkg_cache', ignore_errors=True)
        shutil.rmtree('pip_cache', ignore_errors=True)        
        
    wpilib.run(CleanRobot)
