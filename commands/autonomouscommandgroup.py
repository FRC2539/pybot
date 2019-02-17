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

from commands.drivetrain.newrampingspeedcommand import NewRampingSpeedCommand
from commands.drivetrain.visionmovecommand import visionmoveCommand
from commands.drivetrain.leaverampcommand import leaveRampCommand

class AutonomousCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Autonomous')

        ds = DriverStation.getInstance()

        #find tape and go to it


        #leave ramp
        self.addSequential(leaveRampCommand(20,50,24,80,30,15))
        #self.addSequential(leaveRampCommand(0,50,0,40,1,-35))

        #vision move to tape
        self.addSequential(visionmoveCommand())






        #backup and turn from rocket
        #self.addSequential(leaveRampCommand(-35,50,-24,100,.01,160))

        #self.addSequential(leaveRampCommand(35,35,12,90,0,0))
        #self.addSequential(leaveRampCommand(35.843219,60,45,100,50,36.236817265))


        #self.addSequential(leaveRampCommand(35,85,10,130,90,90))
        #self.addSequential(IntakeCommand(), 10)

        #self.addSequential(StateMachineTempCommand())

        #self.addSequential(NewRampingSpeedCommand(60, 600))

        #self.addSequential(PivotCommand(20))

        '''
        #self.addSequential(SetSpeedCommand(1500))
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
