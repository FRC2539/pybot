import wpilib
import magicbot

import controller.logicalaxes
import ports

from statemachines.driverobotmachine import DriveRobotMachine

from components.drivebase.robotdrive import RobotDrive

from controller.logitechdualshock import LogitechDualshock
from controller.buildlayout import BuildLayout

from ctre import WPI_TalonSRX

import shutil, sys

class CleanRobot(magicbot.MagicRobot):
    driverobotmachine = DriveRobotMachine

    robotdrive = RobotDrive

    def createObjects(self):

        self.motors = [
                WPI_TalonSRX(0),
                WPI_TalonSRX(1),
                WPI_TalonSRX(2),
                WPI_TalonSRX(3)
                ]

        self.layout = BuildLayout(0)

    def teleopInit(self):
        ''' Starts at the beginning of teleop (initialize) '''

    def teleopPeriodic(self):
        self.driverobotmachine.beginDrive()
        ''' Starts on each iteration of the control loop (execute) '''


    
    
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'deploy':
        shutil.rmtree('opkg_cache', ignore_errors=True)
        shutil.rmtree('pip_cache', ignore_errors=True)        
        
    wpilib.run(CleanRobot)
