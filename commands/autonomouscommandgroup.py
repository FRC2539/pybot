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
            self.addSequential(MoveCommand(108))
            
        # Collect balls from our trench
        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'CollectFromTrench')
        def collectFromTrench(self):
            self.addSequential(PrintCommand("CollectFromTrench"))
            self.addSequential(MoveCommand(60))
            #   Shoots initial balls
            self.addSequential(SudoCommandGroup(), 10)
            #   Pick up balls in our trench
            self.addParallel(LowerIntakeCommand())
            self.addParallel(SetSlowCommand())
            self.addParallel(EnableAutoCheckCommand())
            self.addParallel(IntakeCommand())
            self.addSequential(MoveWhileIntakingCommandGroup(186))
            #   Move towards goal
            self.addSequential(MoveCommand(-186))
            self.addSequential(TurnCommand(-15))
            self.addSequential(SudoCommandGroup(), 10)
            
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
            
            
      
