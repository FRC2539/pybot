import wpilib
import magicbot

import controller.logicalaxes
import ports

from custom.config import Config

#from statemachines.drivetrain.driverobotmachine import DriveRobotMachine

from components.drivebase.robotdrive import RobotDrive
from components.drivebase.drivevelocities import TankDrive

from components.falcon.falconcomponent import FalconTest

#from statemachines.drivetrain.movemachine import MoveStateMachine

from controller.logitechdualshock import LogitechDualshock
from controller.buildlayout import BuildLayout

from ctre import TalonFX, TalonFXFeedbackDevice, NeutralMode, WPI_TalonSRX
from rev import CANSparkMax, MotorType

import shutil, sys
import collections

class KryptonBot(magicbot.MagicRobot):
    #smartcargointake: SmartIntake
#cargooutake: CargoOutake

    robotdrive: RobotDrive
    velocity: TankDrive

    falcon: FalconTest

    #movemachine: MoveStateMachine

    def createObjects(self):

        #self.compBot =  Config('DriveTrain/Robot', True) # Make this tunable or nt value
        self.compBot = False

        self.notSoFunCustomDrivebaseStuff()

        self.robotdrive_rumble = False

        '''
        Example:

        self.functionsD = [('LeftTrigger', 'getPositions()', 'self.robotdrive'),
                           ('RightTrigger', 'runOutake()', 'self.cargooutake')
                          ]
        self.functionsO = [
                           ('RightBumper', 'armUp()', 'self.arm'),
                           ('RightTrigger', 'armDown()', 'self.arm'),
                           ('Y', 'elevatorUp()', 'self.elevator'),
                           ('X', 'elevatorDown()', 'self.elevator'),
                           ('A', 'runSmartIntake()', 'self.smartcargointake')
                          ]
        '''
        self.functionsD = []
        self.functionsO = []

        self.falconTest = TalonFX(ports.FalconTest.motorID)
        self.falconTest.configSelectedFeedbackSensor(TalonFXFeedbackDevice.IntegratedSensor, 0, 0)

        self.velocityCalculator = TankDrive()

        self.tolerance = 20

        self.build = BuildLayout(0, 1, self.functionsD, self.functionsO) # USE

        self.build.checkEarly()

        self.useActives = []

    def teleopInit(self):
        self.robotdrive.prepareToDrive(self.compBot)

        #self.movemachine.moveMachineStart(12)

        self.falcon.run()
        ''' Starts at the beginning of teleop (initialize) '''

        #self.movemachine.moveMachineStart(36)

    def teleopPeriodic(self):
        res, _class, release = self.build.checkDriver()
        if type(res) is str and release != 'released':
            eval(str(_class) + '.' + str(res)) # Really sketchy. Freaky sketchy. And I wrote this lol.
        elif type(res) is str:
            eval(str(_class) + '.' + 'default()')

        resO, _classO, releaseO = self.build.checkOperator()
        if type(resO) is str and releaseO != 'released':
            eval(str(_classO) + '.' + str(resO))

        elif type(resO) is str and releaseO == 'released':
            eval(str(_classO) + '.' + 'default()')

        ''' Starts on each iteration of the control loop (execute) (I think I only put high levels here.) '''

    def notSoFunCustomDrivebaseStuff(self):
        if self.compBot:
            try:

                self.robotdrive_motors = [
                        TalonFX(ports.DrivetrainPorts.FrontLeftMotor),
                        TalonFX(ports.DrivetrainPorts.FrontRightMotor),
                        TalonFX(ports.DrivetrainPorts.BackLeftMotor),
                        TalonFX(ports.DrivetrainPorts.BackRightMotor)
                        ]

            except(AttributeError):
                self.robotdrive_motors = [
                        TalonFX(ports.DrivetrainPorts.LeftMotor),
                        TalonFX(ports.DrivetrainPorts.RightMotor)
                        ]

            for motor in self.robotdrive_motors:
                motor.setNeutralMode(NeutralMode.Brake)
                motor.configSelectedFeedbackSensor(TalonFXFeedbackDevice.IntegratedSensor, 0, 0)
        else:
            self.neo_encoders = []
            self.neo_controllers = []

            try:
                self.robotdrive_motors = [
                        CANSparkMax(ports.DrivetrainPorts.FrontLeftMotor, MotorType.kBrushless),
                        CANSparkMax(ports.DrivetrainPorts.FrontRightMotor, MotorType.kBrushless),
                        CANSparkMax(ports.DrivetrainPorts.BackLeftMotor, MotorType.kBrushless),
                        CANSparkMax(ports.DrivetrainPorts.BackRightMotor, MotorType.kBrushless)
                        ]

            except(AttributeError):
                self.robotdrive_motors = [
                        CANSparkMax(ports.DrivetrainPorts.FrontLeftMotor, MotorType.kBrushless),
                        CANSparkMax(ports.DrivetrainPorts.FrontRightMotor, MotorType.kBrushless)
                        ]

            for motor in self.robotdrive_motors:
                self.neo_controllers.append(motor.getPIDController())
                self.neo_encoders.append(motor.getEncoder())

                motor.getEncoder().setPosition(0.0)
                motor.setIdleMode(CANSparkMax.IdleMode.kBrake)

    
    
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'deploy':
        shutil.rmtree('opkg_cache', ignore_errors=True)
        shutil.rmtree('pip_cache', ignore_errors=True)        

    wpilib.run(KryptonBot)
