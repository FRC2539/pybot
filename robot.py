import wpilib
import magicbot

import controller.logicalaxes
import ports

from statemachines.driverobotmachine import DriveRobotMachine

from components.drivebase.robotdrive import RobotDrive
from components.drivebase.drivevelocities import TankDrive

from components.arm.arm import Arm

from components.elevator.elevator import Elevator

from statemachines.movemachine import MoveStateMachine

from controller.logitechdualshock import LogitechDualshock
from controller.buildlayout import BuildLayout

from ctre import WPI_TalonSRX
from rev import CANSparkMax, MotorType

import shutil, sys
import collections

class CleanRobot(magicbot.MagicRobot):
    movemachine: MoveStateMachine

    robotdrive: RobotDrive
    velocity: TankDrive

    arm: Arm

    elevator: Elevator

    def createObjects(self):

        self.robotdrive_motors = [
                WPI_TalonSRX(ports.DrivetrainPorts.FrontLeftMotor),
                WPI_TalonSRX(ports.DrivetrainPorts.FrontRightMotor),
                WPI_TalonSRX(ports.DrivetrainPorts.BackLeftMotor),
                WPI_TalonSRX(ports.DrivetrainPorts.BackRightMotor)
                ]

        self.robotdrive_rumble = False

        self.arm_motor = CANSparkMax(ports.Arm.ArmMotorID, MotorType.kBrushless)
        self.arm_lowerLimit = wpilib.DigitalInput(ports.Arm.lowerLimit)
        self.arm_encoder = self.arm_motor.getEncoder()
        self.arm_pidcontroller = self.arm_motor.getPIDController()

        self.elevator_motor = CANSparkMax(ports.Elevator.ElevatorMotorID, MotorType.kBrushless)
        self.elevator_lowerlimit = wpilib.DigitalInput(ports.Elevator.lowerLimit)
        self.elevator_encoder = self.elevator_motor.getEncoder()
        self.elevator_pidcontroller = self.elevator_motor.getPIDController()

        self.functionsD = [('LeftTrigger', 'getPositions()', 'self.robotdrive')]
        self.functionsO = [
                           ('RightBumper', 'armUp()', 'self.arm'),
                           ('RightTrigger', 'armDown()', 'self.arm'),
                           ('Y', 'elevatorUp()', 'self.elevator'),
                           ('X', 'elevatorDown()', 'self.elevator')
                          ]

        self.velocityCalculator = TankDrive()

        self.activeMotors = self.robotdrive_motors[0:2]

        self.tolerance = 20

        self.build = BuildLayout(0, 1, self.functionsD, self.functionsO) # USE

        self.build.checkEarly()

        self.useActives = []

    def teleopInit(self):
        self.robotdrive.prepareToDrive()
        self.arm.prepareArm()
        self.elevator.prepareElevator()
        ''' Starts at the beginning of teleop (initialize) '''

        self.movemachine.moveMachineStart(36)

    def teleopPeriodic(self):
        res, _class = self.build.checkDriver()
        if type(res) is str:
            eval(str(_class) + '.' + str(res)) # Really sketchy. Freaky sketchy. And I wrote this lol.

        ''' Starts on each iteration of the control loop (execute) (I think I only put high levels here.) '''


    
    
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'deploy':
        shutil.rmtree('opkg_cache', ignore_errors=True)
        shutil.rmtree('pip_cache', ignore_errors=True)        
        
    wpilib.run(CleanRobot)
