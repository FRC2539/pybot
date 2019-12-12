import wpilib
import magicbot

import controller.logicalaxes
import ports

from statemachines.driverobotmachine import DriveRobotMachine

from components.drivebase.robotdrive import RobotDrive
from components.drivebase.drivevelocities import TankDrive

from controller.logitechdualshock import LogitechDualshock
from controller.buildlayout import BuildLayout

from ctre import WPI_TalonSRX

import shutil, sys

class CleanRobot(magicbot.MagicRobot):
    #driverobotmachine = DriveRobotMachine

    robotdrive = RobotDrive

    def createObjects(self):

        self.robotdrive_motors = [
                WPI_TalonSRX(ports.DrivetrainPorts.FrontLeftMotor),
                WPI_TalonSRX(ports.DrivetrainPorts.FrontRightMotor),
                WPI_TalonSRX(ports.DrivetrainPorts.BackLeftMotor),
                WPI_TalonSRX(ports.DrivetrainPorts.BackRightMotor)
                ]

        self.driveLayout = {'A' : self.robotdrive.getSpeeds}

        self.velocityCalculator = TankDrive(rotateModifier=0.7)

        self.activeMotors = self.velocityCalculator.configureFourTank(self.robotdrive_motors)

        self.build = BuildLayout(0, self.driveLayout)


    def teleopInit(self):
        self.robotdrive.prepareToDrive()
        ''' Starts at the beginning of teleop (initialize) '''

    def teleopPeriodic(self):
        ''' Starts on each iteration of the control loop (execute) (I think I only put high levels here.) '''


    
    
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'deploy':
        shutil.rmtree('opkg_cache', ignore_errors=True)
        shutil.rmtree('pip_cache', ignore_errors=True)        
        
    wpilib.run(CleanRobot)
