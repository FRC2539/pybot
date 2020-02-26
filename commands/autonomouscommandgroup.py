from wpilib.command import CommandGroup
from wpilib import DriverStation as _ds

from networktables import NetworkTables

import commandbased.flowcontrol as fc
from custom.config import Config

from commands.network.alertcommand import AlertCommand

from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.turncommand import TurnCommand

from commands.hood.setlaunchanglecommand import SetLaunchAngleCommand

from commands.shooter.shootcommand import ShootCommand
from commands.shooter.controlledshootcommand import ControlledShootCommand
from commands.shooter.stopshootercommand import StopShooterCommand

from commands.colorwheel.autosetwheel import AutoSetWheelCommand

from commands.limelight.sudocommandgroup import SudoCommandGroup

from commands.ballsystem.rununtilloadedcommand import RunUntilLoadedCommand
from commands.ballsystem.runballflowcommandgroup import RunBallFlowCommandGroup
from commands.ballsystem.rununtilemptycommand import RunUntilEmptyCommand

from commands.turret.setturretcommand import SetTurretCommand
from commands.turret.turretlimelightcommand import TurretLimelightCommand

from commands.intake.intakecommand import IntakeCommand

class AutonomousCommandGroup(fc.CommandFlow):
    def __init__(self):
        super().__init__('Autonomous')

        startingBalls = 3#Config('Autonomous/NumberOfBallsAtStart', 3)
        print('SET STUFFF ' + str(Config('Autonomous/autoModeSelect', None)))


        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == '3 Ball Auto') # Put given game data here through network tables.
        def ThreeBallAuto(self):#should be good for now
            self.addParallel(ShootCommand(3400))
            self.addParallel(SetLaunchAngleCommand(26.0))
            self.addSequential(SetTurretCommand(2100), 3)
            self.addSequential(TurretLimelightCommand(), .5)
            self.addParallel(TurretLimelightCommand())
            self.addParallel(IntakeCommand(0.2))
            self.addSequential(RunBallFlowCommandGroup(), 5)
            self.addParallel(StopShooterCommand())
            self.addSequential(MoveCommand(30))

        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == '5 Ball Auto')
        def rennaFirstFunctionButMore(self):
            self.addParallel(SetTurretCommand(2100), 3)
            self.addParallel(IntakeCommand(), 5)
            self.addSequential(MoveCommand(55))
            self.addSequential(MoveCommand(25))
            self.addSequential(SudoCommandGroup(),1)
            self.addParallel(SudoCommandGroup(.4))
            self.addParallel(ShootCommand(4200), 8)
            self.addSequential(RunUntilEmptyCommand(5), 6)

        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == '6 Ball Auto')
        def rennaFirstFunction(self):
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


        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'SkSkSkirt off the init line')
        def getOffInitLine(self):
            print("sksksk")#start station 2, shoot balls, run to generator
            self.addParallel(SetTurretCommand(2100), 3)
            self.addSequential(MoveCommand(90))
            self.addParallel(SudoCommandGroup(), 4)
            self.addParallel(ShootCommand(4200), 8)
            self.addSequential(RunUntilEmptyCommand(startingBalls))
            self.addSequential(TurnCommand(180)) #Turn to face generator
            self.addSequential(MoveCommand(90))

        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'shootie trench')
        def shootTrench(self):
            print("shootieTrench")
            self.addSequential(MoveCommand(90))
            self.addParallel(SetTurretCommand(2100), 3)
            self.addParallel(SudoCommandGroup(), 4)
            self.addParallel(ShootCommand(4200), 8)
            self.addSequential(RunUntilEmptyCommand(startingBalls))
            #finish


