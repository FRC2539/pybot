import wpilib
import magicbot

import controller.logicalaxes
import ports

from components.drivebase.robotdrive import RobotDrive

from controller.logitechdualshock import LogitechDualshock
from controller.buildlayout import BuildLayout

from ctre import WPI_TalonSRX

import shutil, sys

class CleanRobot(magicbot.MagicRobot):
    
    def createObjects(self):
        self.drivetrain = RobotDrive('tank') # creates a drivetrain object

        self.drivetrainMotors = [
                    WPI_TalonSRX(ports.DrivetrainPorts.FrontLeftMotor),
                    WPI_TalonSRX(ports.DrivetrainPorts.FrontRightMotor),
                    WPI_TalonSRX(ports.DrivetrainPorts.BackLeftMotor),
                    WPI_TalonSRX(ports.DrivetrainPorts.BackRightMotor)
                    ]
        ''' Create motors and stuff here (init)'''    
        
        self.layout = BuildLayout(0)
        self.controller = self.layout.returnObj()
            
    def teleopInit(self):
        ''' Starts at the beginning of teleop (initialize) '''

        self.drivetrain.registerAxes()
        
    def teleopPeriodic(self):
        ''' Starts on each iteration of the control loop (execute) '''

        self.drivetrain.driveRobot()
    
    
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'deploy':
        shutil.rmtree('opkg_cache', ignore_errors=True)
        shutil.rmtree('pip_cache', ignore_errors=True)        
        
    wpilib.run(CleanRobot)
