from wpilib.command import PrintCommand, WaitCommand
from wpilib import DriverStation as _ds

import commandbased.flowcontrol as fc

from networktables import NetworkTables
from custom.config import Config

#from crapthatwillneverwork.kougarkoursegenerator import KougarKourseGenerator
#from crapthatwillneverwork.kougarkourse import KougarKourse
27.0.0.1/8 scope host lo
       valid_lft forever p
from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.turncommand import TurnCommand
from commands.drivetrain.setspeedcommand import SetSpeedCommand
#from commands.drivetrain.gyromovecommand import GyroMoveCommand
from commands.drivetrain.movewhileintakingcommandgroup import MoveWhileIntakingCommandGroup
from commands.drivetrain.curvecommand import CurveCommand

from commands.intake.loadinemptycommandgroup import LoadInEmptyCommandGroup
from commands.intake.lowerintakecommand import LowerIntakeCommand

from commands.shooter.setrpmcommand import SetRPMCommand
from commands.shooter.stevenshooterlimelightcommand import StevenShooterLimelightCommand

from commands.limelight.sudocommandgroup import SudoCommandGroup

#testTrajectory = KougarKourseGenerator(0)

class AutonomousCommandGroup(fc.CommandFlow):
        
    def __init__(self):
        super().__init__('Autonomous')
        
        #print('auto init: '+ Config('Autonomous/autoModeSelect'))
        #establish the auto modes for dashboard and use these values in auto if string check
        table = NetworkTables.getTable('Autonomous')
        #autoNames = ['Turn', 'Move', 'Move Turn Move', 'CollectFromTrench', 'GetOffLine']
        autoNames = ['GetOffLine', 'CollectFromTrench', 'StealFromTrench', 'Auto1']
        autoString = ''
        for auto in autoNames:
            autoString += str(auto + '$')
        autoString = autoString[:-1]
        table.putString('autoModes', autoString)
        
        #   Gets off the line
        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'GetOffLine')
        def getOffLine(self): # should be good for now
            self.addSequential(MoveCommand(48))
            
        # Collect balls from our trench
        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'CollectFromTrench')
        def collectFromTrench(self):
            self.addSequential(PrintCommand("CollectFromTrench"))
            self.addSequential(MoveCommand(36))
            #   Shoots initial balls
            self.addSequential(SudoCommandGroup(), 10)
            self.addParallel(LowerIntakeCommand())
            self.addSequential(TurnCommand(-45))
            self.addSequential(MoveWhileIntakingCommandGroup(32))
            self.addSequential(TurnCommand(45))
            #   Pick up balls in our trench
            self.addSequential(MoveWhileIntakingCommandGroup(186))
            self.addSequential(MoveCommand(-186))
            self.addSequential(TurnCommand(-15))
            self.addSequential(SudoCommandGroup(), 10)
            
        #   Steals two balls from enemy trench
        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'StealFromTrench')
        def stealFromTrench(self):
            self.addSequential(PrintCommand('StealFromTrench'))
            # Collect Balls
            self.addParallel(LowerIntakeCommand())
            self.addSequential(MoveCommand(84))
            self.addSequential(TurnCommand(52))
            #   Pick up balls in enemy trench
            self.addSequential(MoveWhileIntakingCommandGroup(48))
            self.addSequential(TurnCommand(10))
            self.addSeq uential(MoveCommand(-228))
            self.addSequential(TurnCommand(-60))
            self.addSequential(SudoCommandGroup(), 10)
            
            
      
