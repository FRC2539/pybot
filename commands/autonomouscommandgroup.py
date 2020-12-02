from wpilib.command import PrintCommand, WaitCommand
from wpilib import DriverStation as _ds

import commandbased.flowcontrol as fc

from networktables import NetworkTables
from custom.config import Config

#from crapthatwillneverwork.kougarkoursegenerator import KougarKourseGenerator
#from crapthatwillneverwork.kougarkourse import KougarKourse

from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.turncommand import TurnCommand
from commands.drivetrain.setspeedcommand import SetSpeedCommand
#from commands.drivetrain.gyromovecommand import GyroMoveCommand
from commands.drivetrain.movewhileintakingcommandgroup import MoveWhileIntakingCommandGroup
from commands.drivetrain.curvecommand import CurveCommand
from commands.drivetrain.setslowcommand import SetSlowCommand
from commands.drivetrain.setnormalcommand import SetNormalCommand

from commands.intake.loadinemptycommandgroup import LoadInEmptyCommandGroup
from commands.intake.lowerintakecommand import LowerIntakeCommand
from commands.intake.raiseintakecommand import RaiseIntakeCommand
from commands.intake.intakecommand import IntakeCommand

from commands.pneumatics.disablecompressorcommand import DisableCompressorCommand
from commands.pneumatics.enablecompressorcommand import EnableCompressorCommand

from commands.revolver.enableautocheckcommand import EnableAutoCheckCommand
from commands.revolver.disableautocheckcommand import DisableAutoCheckCommand
from commands.revolver.spinuprevolvercommand import SpinUpRevolverCommand

from commands.shooter.setrpmcommand import SetRPMCommand
from commands.shooter.stevenshooterlimelightcommand import StevenShooterLimelightCommand
from commands.shooter.maketherobotshootballsandonlyshootballscommand import MakeTheRobotShootBallsAndOnlyShootBallsCommand

from commands.limelight.sudocommandgroup import SudoCommandGroup

#testTrajectory = KougarKourseGenerator(0)

class AutonomousCommandGroup(fc.CommandFlow):
        
    def __init__(self):
        super().__init__('Autonomous')
        
        #print('auto init: '+ Config('Autonomous/autoModeSelect'))
        #establish the auto modes for dashboard and use these values in auto if string check
        table = NetworkTables.getTable('Autonomous')
        autoNames = ['GetOffLine', 'CollectFromTrench', 'StealFromTrench']
        autoString = ''
        for auto in autoNames:
            autoString += str(auto + '$')
        autoString = autoString[:-1]
        table.putString('autoModes', autoString)
        
        #   Gets off the line
        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'GetOffLine')
        def getOffLine(self): # should be good for now
            self.addSequential(SetSlowCommand())
            self.addSequential(MoveCommand(60))
            self.addSequential(SetNormalCommand())
            self.addSequential(MoveCommand(-60))
            
        # Collect balls from our trench
        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'CollectFromTrench')
        def collectFromTrench(self):
            self.addSequential(PrintCommand("CollectFromTrench"))
            self.addParallel(DisableCompressorCommand())
            
            #   Shoots initial balls
            self.addParallel(SetRPMCommand(4500))
            self.addSequential(MoveCommand(36))
            self.addSequential(SetSlowCommand())
            self.addSequential(SudoCommandGroup(), 8)
            #   Pick up balls in our trench
            self.addParallel(EnableAutoCheckCommand())
            self.addParallel(IntakeCommand())
            #   Move towards goal
            self.addSequential(MoveCommand(180)) #  8 ball - 216
            self.addSequential(SetNormalCommand())
            self.addParallel(DisableAutoCheckCommand())
            self.addParallel(RaiseIntakeCommand())
            self.addParallel(SetRPMCommand(4500))
            self.addParallel(SpinUpRevolverCommand())
            #   Move towards goal
            self.addSequential(MoveCommand(-144)) # 8 ball - 180
            self.addSequential(SudoCommandGroup(), 10)
            self.addParallel(EnableCompressorCommand())
            
        # Steals two balls from enemy trench
        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'StealFromTrench')
        def stealFromTrench(self):
            self.addParallel(DisableCompressorCommand())
            # Collect Balls
            self.addParallel(LowerIntakeCommand())
            self.addSequential(MoveCommand(54))
            self.addSequential(TurnCommand(30))
            #   Pick up balls in enemy trench
            self.addParallel(SetSlowCommand())
            self.addParallel(EnableAutoCheckCommand())
            self.addParallel(IntakeCommand())
            self.addSequential(MoveCommand(42))
            self.addSequential(TurnCommand(40))
            self.addSequential(MoveCommand(18))
            #   Move towards goal
            self.addParallel(SetNormalCommand())
            self.addParallel(DisableAutoCheckCommand())
            self.addParallel(RaiseIntakeCommand())
            self.addParallel(SetRPMCommand(4000))
            self.addSequential(MoveCommand(-228))
            self.addSequential(TurnCommand(-70))
            self.addSequential(SudoCommandGroup(), 10)
            self.addSequential(MakeTheRobotShootBallsAndOnlyShootBallsCommand())
            self.addParallel(EnableCompressorCommand())
