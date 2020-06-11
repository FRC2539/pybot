from wpilib.command import CommandGroup
from wpilib import DriverStation as _ds

from networktables import NetworkTables

import commandbased.flowcontrol as fc
from custom.config import Config

from commands.network.alertcommand import AlertCommand

from commands.drivetrain.setspeedcommand import SetSpeedCommand
from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.turncommand import TurnCommand
from commands.drivetrain.gyromovecommand import GyroMoveCommand
from commands.drivetrain.resetencoderscommand import ResetEncodersCommand

from commands.hood.setlaunchanglecommand import SetLaunchAngleCommand
from commands.hood.hoodlimelightcommand import HoodLimelightCommand

from commands.shooter.shootcommand import ShootCommand
from commands.shooter.controlledshootcommand import ControlledShootCommand
from commands.shooter.stopshootercommand import StopShooterCommand

from commands.colorwheel.autosetwheel import AutoSetWheelCommand

from commands.limelight.sudocommandgroup import SudoCommandGroup
from commands.limelight.aimturretdrivebasecommand import AimTurretDrivebaseCommand
from commands.limelight.ogsudocommandgroup import OgSudoCommandGroup
from commands.limelight.passcommand import PassCommand

from commands.ballsystem.stopallcommand import StopAllCommand
from commands.ballsystem.endwhenemptycommand import EndWhenEmptyCommand
from commands.ballsystem.rununtilloadedcommand import RunUntilLoadedCommand
from commands.ballsystem.runbasicsystemcommand import RunBasicSystemCommand
from commands.ballsystem.runballflowcommandgroup import RunBallFlowCommandGroup
from commands.ballsystem.rununtilemptycommand import RunUntilEmptyCommand
from commands.ballsystem.runallcommand import RunAllCommand
from commands.ballsystem.clearjamcommand import ClearJamCommand

from commands.turret.setturretcommand import SetTurretCommand
from commands.turret.turretlimelightcommand import TurretLimelightCommand
from commands.turret.turretstartcommandgroup import TurretStartCommandGroup

from commands.intake.intakecommand import IntakeCommand
from commands.intake.stopeverythingcommand import StopEverythingCommand

class AutonomousCommandGroup(fc.CommandFlow):
    def __init__(self):
        super().__init__('Autonomous')

        selectAuto = '6 Ball Auto'

        startingBalls = Config('Autonomous/NumberOfBallsAtStart', 3)

        #@fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == None) # Put given game data here through network tables.
        #def ThreeBallAuto(self):#should be good for now
            ##self.addSequential(GyroMoveCommand(30))
            #self.addParallel(ShootCommand(3400))
            #self.addParallel(SetLaunchAngleCommand(26.0))
            #self.addSequential(SetTurretCommand(2100), 3)
            #self.addSequential(TurretLimelightCommand(), .75)
            #self.addParallel(TurretLimelightCommand())
            #self.addParallel(IntakeCommand(0.2))
            #self.addSequential(RunUntilEmptyCommand(startingBalls), 6)
            ##self.addParallel(StopEverythingCommand())
            #self.addSequential(MoveCommand(15))

        #@fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == '3 Ball Auto') # Put given game data here through network tables.
        #def ThreeBallAuto(self):#should be good for now
            ##self.addSequential(GyroMoveCommand(30))
            #self.addParallel(ShootCommand(3400))
            #self.addParallel(SetLaunchAngleCommand(26.0))
            #self.addSequential(SetTurretCommand(2100), 3)
            #self.addSequential(TurretLimelightCommand(), .75)
            #self.addParallel(TurretLimelightCommand())
            #self.addParallel(IntakeCommand(0.2))
            #self.addSequential(RunUntilEmptyCommand(startingBalls), 6)
            ##self.addParallel(StopEverythingCommand())
            #self.addSequential(MoveCommand(15))

        #@fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == '3 Ball Move First') # Put given game data here through network tables.
        #def ThreeBallMoveFirst(self):#should be good for now
            #self.addParallel(ShootCommand(3500))
            #self.addParallel(SetTurretCommand(2100), 3)
            #self.addSequential(MoveCommand(38), 2.5) # possibly not ending?
            ##self.addSequential(AimTurretDrivebaseCommand(), .5)
            #self.addSequential(HoodLimelightCommand(), 1) # referencing hood and not ending, thus prohibiting the sudo cg?
            #self.addSequential(TurretLimelightCommand(), 0.5)
            #self.addParallel(TurretLimelightCommand())
            #self.addParallel(IntakeCommand(0.2))
            #self.addSequential(RunAllCommand(), 6)
            #self.addSequential(StopEverythingCommand())

        #@fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == '5 Ball Auto')
        #def FiveBallAuto(self):
            #self.addParallel(ShootCommand(3700))
            #self.addParallel(SetTurretCommand(2100), 3)
            #self.addParallel(IntakeCommand(), 5)
            #self.addSequential(MoveCommand(145))
            #self.addSequential(SudoCommandGroup(), .5)
            #self.addParallel(SudoCommandGroup())
            #self.addParallel(ShootCommand(4200), 8)
            #self.addSequential(RunUntilEmptyCommand(5), 6)
            #self.addSequential(StopEverythingCommand())
## WORKING 6 BALLS
        @fc.IF(lambda: True)
        def SixBallAuto(self):
            self.addSequential(TurnCommand(180))
            #self.addSequential(SetSpeedCommand(5500))
            #self.addParallel(ShootCommand(4200))
            #self.addParallel(TurretStartCommandGroup())
            #self.addSequential(MoveCommand(74))
             ## should remain running
            #self.addParallel(RunUntilLoadedCommand(), 10)
            #self.addSequential(RunUntilEmptyCommand(startingBalls), 5)
            #self.addSequential(MoveCommand(110), 3)
            #self.addParallel(ResetEncodersCommand())
            #self.addSequential(MoveCommand(-110), 3) # gives plenty of time to shoot until its empty.
            #self.addSequential(RunUntilEmptyCommand(3), 6)
            #self.addSequential(SetSpeedCommand(10250))
            #self.addParallel(StopEverythingCommand())


        #@fc.IF(lambda: True)
        #def SixBallAuto(self):
            ##self.addSequential(SetSpeedCommand(5500))
            ##self.addParallel(ShootCommand(4200))
            ##self.addParallel(TurretStartCommandGroup())
            #self.addSequential(TurnCommand(90), 2)
            #self.addSequential(TurnCommand(-90), 2)
            #self.addSequential(MoveCommand(110))
            #self.addSequential(TurnCommand(-180), 1.75)
            #self.addSequential(MoveCommand(-25))
            #self.addSequential(TurnCommand(360), 3)
            #self.addSequential(MoveCommand(-50))
            #self.addSequential(TurnCommand(90),3)
