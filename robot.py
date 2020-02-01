#!/usr/bin/env python3

import wpilib
import magicbot

from magicbot.magic_tunable import tunable, setup_tunables

import controller.logicalaxes
import ports

from custom.config import Config

#from statemachines.drivetrain.driverobotmachine import DriveRobotMachine

from statemachines.intake.intakeballs import IntakeBallsCommand
from statemachines.intake.outakeballs import OutakeBallsCommand

from components.potentiometer import Potentiometer

from components.drivebase.robotdrive import RobotDrive
from components.drivebase.drivevelocities import TankDrive

from components.turret import Turret

from components.hood import Hood

from components.shooter import Shooter

from components.falcon.falconcomponent import FalconTest

from components.intake import Intake

from components.colorwheel import ColorWheel

from components.limelight import Limelight

#from statemachines.drivetrain.movemachine import MoveStateMachine

from controller.logitechdualshock import LogitechDualshock
from controller.buildlayout import BuildLayout

from ctre import TalonFX, TalonFXFeedbackDevice, NeutralMode, WPI_TalonSRX

from rev import CANSparkMax, MotorType
from rev.color import ColorSensorV3

import shutil, sys
import collections

class KryptonBot(magicbot.MagicRobot):
    robotdrive: RobotDrive
    velocity: TankDrive

    intakecommand: IntakeBallsCommand
    #outtakecommand: OutakeBallsCommand

    falcon: FalconTest

    potent: Potentiometer

    shooter: Shooter

    hood: Hood

    turret: Turret

    wheelactions: ColorWheel

    intake: Intake

    limelight: Limelight

    #movemachine: MoveStateMachine

    @classmethod
    def createGenerators(cls):
        try:
            sys.modules['robot'].ColorWheel = ColorWheel()
        except KeyError:
            pass

    def createObjects(self):

        #self.bot =  Config('DriveTrain/Robot', True) # Make this tunable or nt value
        self.bot = tunable(False)

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
        self.functionsD = [('A', 'intakeCommand()', 'self.intakecommand')]

        self.functionsO = [('A', 'intakeCommand()', 'self.intakecommand')]

        self.falconTest = TalonFX(ports.FalconTest.motorID)
        self.falconTest.configSelectedFeedbackSensor(TalonFXFeedbackDevice.IntegratedSensor, 0, 0)

        self.intakeMotor = CANSparkMax(ports.IntakePorts.motorID, MotorType.kBrushed)
        self.intakeRunning = False

        self.loadSystemMotor = CANSparkMax(ports.LoadSystemPorts.motorID, MotorType.kBrushed)

        self.colorSensor = ColorSensorV3(wpilib.I2C.Port.kOnboard)
        self.colorWheelMotor = CANSparkMax(ports.ColorWheelPorts.motorID, MotorType.kBrushless)# WPI_TalonSRX(ports.ColorWheelPorts.motorID)
        self.colorWheelEncoder = self.colorWheelMotor.getEncoder()
        self.colorWheelController = self.colorWheelMotor.getPIDController()

        self.velocityCalculator = TankDrive()

        self.shooterMotor = CANSparkMax(ports.ShooterPorts.motorID, MotorType.kBrushless)

        self.hoodMotor = CANSparkMax(ports.HoodPorts.motorID, MotorType.kBrushless)

        self.turretMotor = WPI_TalonSRX(ports.TurretPorts.motorID)

        self.potentiometer = wpilib.AnalogPotentiometer(0)
        self.potentiometerTalon = CANSparkMax(2, MotorType.kBrushed)

        self.potentiometerForward = wpilib.DigitalInput(0)
        self.potentiometerReverse = wpilib.DigitalInput(1)

        self.potentiometerOne = wpilib.DigitalInput(6)
        self.potentiometerTwo = wpilib.DigitalInput(7)
        self.potentiometerThree = wpilib.DigitalInput(8)
        self.potentiometerFour = wpilib.DigitalInput(9)

        self.tolerance = 20

        self.build = BuildLayout(0, 1, self.functionsD, self.functionsO) # USE

        self.build.checkEarly()

        self.useActives = []

        #self.createGenerators()

        print('complete')

    def teleopInit(self):
        self.potent.setup()

        self.robotdrive.prepareToDrive()
        self.robotdrive.assignFuncs()

        self.limelight.setup()

        self.shooter.setup()

        self.hood.setup()

        #self.movemachine.moveMachineStart(12)

        #self.falcon.run()
        ''' Starts at the beginning of teleop (initialize) '''

        #self.movemachine.moveMachineStart(36)

    def teleopPeriodic(self):
        res, _class, release = self.build.checkDriver()
        if type(res) is str and release != 'held':
            eval(str(_class) + '.' + str(res)) # Really sketchy. Freaky sketchy. And I wrote this lol.
        #elif type(res) is str:
            #eval(str(_class) + '.' + 'default()')

        resO, _classO, releaseO = self.build.checkOperator()
        if type(resO) is str and releaseO != 'held':
            eval(str(_classO) + '.' + str(resO))

        #elif type(resO) is str:
            #eval(str(_classO) + '.' + 'default()')

        ''' Starts on each iteration of the control loop (execute) (I think I only put high levels here.) '''

    def notSoFunCustomDrivebaseStuff(self):
        if self.bot:
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
