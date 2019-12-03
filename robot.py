import wpilib
import magicbot

import controller.logicalaxes
import ports

from statemachines.driverobot import DriveRobot

from components.drivebase.robotdrive import RobotDrive

from controller.logitechdualshock import LogitechDualshock
from controller.buildlayout import BuildLayout

from ctre import WPI_TalonSRX

import shutil, sys

class CleanRobot(magicbot.MagicRobot):    
    drivetrain = RobotDrive
    
    def createObjects(self):
        self.frontLeftMotor = WPI_TalonSRX(0)
        self.frontRightotor = WPI_TalonSRX(1)
        self.backLeftMotor = WPI_TalonSRX(2)
        self.backRightMotor = WPI_TalonSRX(3)
        
        self.layout = BuildLayout(0)
        self.controller = self.layout.returnObj()
            
    def teleopInit(self):
        ''' Starts at the beginning of teleop (initialize) '''
        #self.drivetrain.beginDrive()
        pass
    def teleopPeriodic(self):
        ''' Starts on each iteration of the control loop (execute) '''

        self.drivetrain.beginDrive()
    
    
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'deploy':
        shutil.rmtree('opkg_cache', ignore_errors=True)
        shutil.rmtree('pip_cache', ignore_errors=True)        
        
    wpilib.run(CleanRobot)
