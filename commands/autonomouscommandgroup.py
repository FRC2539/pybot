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
        print('as ' + str(Config('Autonomous/autoModeSelect','nope')))
            
        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'GetOffLine')
        def getOffLine(self): # should be good for now
            self.addSequential(PrintCommand("Get Off Line"))
            # get off line
            self.addSequential(MoveCommand(48))#MoveWhileIntakingCommandGroup(120))

        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'CollectFromTrench')
        def collectFromTrench(self):#should be good for now
            self.addSequential(PrintCommand("CollectFromTrench"))
            #power shooter
            self.addSequential(MoveCommand(36))
            
            #shoot
            #lower intake
            #power shooter
            
            self.addSequential(TurnCommand(-45))
            self.addSequential(MoveCommand(32))
            self.addSequential(TurnCommand(45))
            self.addSequential(MoveCommand(186))
            #pick up balls 
            
            self.addSequential(MoveCommand(-186))
            self.addSequential(TurnCommand(-15))
            #shoot
            
            
            # Steal from enemy trench
        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'StealFromTrench')
        def stealFromTrench(self):
            self.addSequential(PrintCommand('StealFromTrench'))
            # Collect Balls
            self.addParallel(LowerIntakeCommand())
            self.addSequential(MoveCommand(84))
            self.addSequential(TurnCommand(52))
            self.addSequential(MoveWhileIntakingCommandGroup(48))
            # Move to shoot
            self.addSequential(TurnCommand(10))
            self.addSequential(MoveCommand(-228))
            self.addSequential(TurnCommand(-62))
            #self.addSequential(SudoCommandGroup(), 10)
            
            
        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'Move Turn Move')
        def MTM(self):
            self.addSequential(PrintCommand("Move Turn Move"))
            self.addSequential(MoveCommand(40), 2)
            self.addSequential(TurnCommand(90), 2)
            self.addSequential(MoveCommand(-40), 2)

        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect')) == 'Auto1')
        def auto1(self):#should be good for now
            self.addSequential(SudoCommandGroup(), 10)
            ##self.addSequential(PrintCommand("Auto 1"))
            ##self.addSequential(MoveCommand(80))
            
            ##self.addSequential(TurnCommand(90))
            #self.addSequential(CurveCommand(-125, 30, False))
            ##self.addSequential(CurveCommand(-130, 30, True))
            #self.addSequential(MoveCommand(45))
            ##self.addSequential(MoveCommand(-45))
