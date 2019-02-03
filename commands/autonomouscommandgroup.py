from wpilib.command import CommandGroup
from wpilib.command import PrintCommand
from wpilib.driverstation import DriverStation
from custom.config import Config
from commands.network.alertcommand import AlertCommand
from wpilib.command.waitcommand import WaitCommand
import commandbased.flowcontrol as fc

from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.movewithgyrocommand import MoveWithGyroCommand
from commands.drivetrain.pivotcommand import PivotCommand
from commands.drivetrain.turncommand import TurnCommand
from commands.drivetrain.runintowallcommand import RunIntoWallCommand
from commands.drivetrain.setspeedcommand import SetSpeedCommand
from commands.drivetrain.gotowallcommand import GoToWallCommand
from commands.elevator.gotoheightcommand import GoToHeightCommand
from commands.intake.intakecommand import IntakeCommand
from commands.intake.outtakecommand import OuttakeCommand
from commands.intake.slowouttakecommand import SlowOuttakeCommand

from commands.drivetrain.statemachinetempcommand import StateMachineTempCommand

class AutonomousCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Autonomous')

        ds = DriverStation.getInstance()

        #self.addSequential(SetSpeedCommand(800))

        self.addParallel(StateMachineTempCommand())


        #self.addSequential(PivotCommand(20))

        '''
        self.addSequential(SetSpeedCommand(1500))
        self.addSequential(PivotCommand(45), 2)
        self.addParallel(GoToHeightCommand('switch'))
        self.addParallel(IntakeCommand(), 10)
        self.addSequential(MoveWithGyroCommand(130))
        self.addSequential(PivotCommand(-45), 2)
        self.addSequential(OuttakeCommand(), 0.5)
        self.addSequential(MoveWithGyroCommand(-10))
        self.addSequential(SetSpeedCommand(800))
        self.addSequential(GoToHeightCommand('ground'))
        '''
