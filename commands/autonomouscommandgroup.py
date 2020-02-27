from wpilib.command import CommandGroup
from wpilib import DriverStation as _ds

from networktables import NetworkTables

import commandbased.flowcontrol as fc
from custom.config import Config

from commands.network.alertcommand import AlertCommand

from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.turncommand import TurnCommand
from commands.drivetrain.gyromovecommand import GyroMoveCommand

from commands.hood.setlaunchanglecommand import SetLaunchAngleCommand

from commands.shooter.shootcommand import ShootCommand
from commands.shooter.controlledshootcommand import ControlledShootCommand
from commands.shooter.stopshootercommand import StopShooterCommand

from commands.colorwheel.autosetwheel import AutoSetWheelCommand

from commands.limelight.sudocommandgroup import SudoCommandGroup
from commands.limelight.aimturretdrivebasecommand import AimTurretDrivebaseCommand

from commands.ballsystem.rununtilloadedcommand import RunUntilLoadedCommand
from commands.ballsystem.runballflowcommandgroup import RunBallFlowCommandGroup
from commands.ballsystem.rununtilemptycommand import RunUntilEmptyCommand

from commands.turret.setturretcommand import SetTurretCommand
from commands.turret.turretlimelightcommand import TurretLimelightCommand

from commands.intake.intakecommand import IntakeCommand
from commands.intake.stopeverythingcommand import StopEverythingCommand

class AutonomousCommandGroup(fc.CommandFlow):
    def __init__(self):
        super().__init__('Autonomous')

        startingBalls = Config('Autonomous/NumberOfBallsAtStart', 3)
        print('SET STUFFF ' + str(Config('Autonomous/autoModeSelect', None)))


        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == '3 Ball Auto') # Put given game data here through network tables.
        def ThreeBallAuto(self):#should be good for now
            #self.addSequential(GyroMoveCommand(30))
            self.addParallel(ShootCommand(3400))
            self.addParallel(SetLaunchAngleCommand(26.0))
            self.addSequential(SetTurretCommand(2100), 3)
            self.addSequential(TurretLimelightCommand(), .5)
            self.addParallel(TurretLimelightCommand())
            self.addParallel(IntakeCommand(0.2))
            self.addSequential(RunUntilEmptyCommand(), 8)
            self.addParallel(StopEverythingCommand())
            self.addSequential(GyroMoveCommand(15))

        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == '3 Ball Move First') # Put given game data here through network tables.
        def ThreeBallMoveFirst(self):#should be good for now
            self.addParallel(ShootCommand(3400))
            self.addParallel(SetLaunchAngleCommand(26.0))
            self.addParallel(SetTurretCommand(2100), 3)
            self.addSequential(GyroMoveCommand(30))
            self.addSequential(AimTurretDrivebaseCommand(), .5)
            self.addParallel(SudoCommandGroup())
            self.addParallel(IntakeCommand(0.2))
            self.addSequential(RunBallFlowCommandGroup(), 5)
            self.addSequential(StopEverythingCommand())

        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == '5 Ball Auto')
        def FiveBallAuto(self):
            self.addParallel(SetTurretCommand(2100), 3)
            self.addParallel(IntakeCommand(), 5)
            self.addSequential(MoveCommand(145))
            self.addSequential(SudoCommandGroup(), .5)
            self.addParallel(SudoCommandGroup())
            self.addParallel(ShootCommand(4200), 8)
            self.addSequential(RunUntilEmptyCommand(5), 6)
            self.addSequential(StopEverythingCommand())

        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == '6 Ball Auto')
        def SixBallAuto(self):
            print ("I Shoot")#station 3 shoot balls pick up 3 in trench
            self.addParallel(ShootCommand(3400))
            self.addParallel(SetLaunchAngleCommand(26.0))
            self.addSequential(SetTurretCommand(2100), 3)
            self.addSequential(TurretLimelightCommand(), .5)
            self.addParallel(TurretLimelightCommand())
            self.addParallel(IntakeCommand(0.2))
            self.addSequential(RunBallFlowCommandGroup(), 5)
            self.addParallel(StopShooterCommand())
            self.addSequential(MoveCommand(55))
            self.addSequential(MoveCommand(25))
            self.addSequential(SudoCommandGroup(),1)
            self.addParallel(SudoCommandGroup())
            self.addParallel(ShootCommand(4200), 8)
            self.addSequential(RunUntilEmptyCommand(5), 6)
            self.addSequential(StopEverythingCommand())
