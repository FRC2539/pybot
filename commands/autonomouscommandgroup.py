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

from commands.drivetrain.movewithgyrocommand import MoveWithGyroCommand
from commands.drivetrain.zerogyrocommand import ZeroGyroCommand
from commands.drivetrain.newrampingspeedcommand import NewRampingSpeedCommand
from commands.drivetrain.visionmovecommand import visionmoveCommand
from commands.drivetrain.leaverampcommand import LeaveRampCommand

class AutonomousCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Autonomous')

        ds = DriverStation.getInstance()

        ###visionmove demo
        self.addSequential(visionmoveCommand(True))

        ###go to rocket then go to ham play place
        #self.addSequential(LeaveRampCommand(30,60,30,260,1,45))
        #self.addSequential(LeaveRampCommand(-50,60,-60,220,1,145))

        ###cargoship to place first hatch then go to ham play place
        #self.addSequential(LeaveRampCommand(30,60,30,240,1,-30))
        #self.addSequential(TurnCommand(160))
        #self.addSequential(LeaveRampCommand(30,60,30,270,140,50))
        #self.addSequential(visionmoveCommand())



        #slowspeed,highspeed,transitionDistance,endDistance,rotateDistance=0,degrees=0
        #rotateDistance must be higher than transitionDistance for it to continue moving after the rotation.
        #if rotatedistance is above 30, it moves until it hits the wall. IF rotateDistance is below 30, it moves the same small distance every time.
        #we have no control over when it turn

        #start right to rocket1
        #self.addParallel(ZeroGyroCommand())
        #self.addSequential(LeaveRampCommand())

        #start right to rocket2
        #self.addParallel(ZeroGyroCommand))
        #self.addSequential(LeaveRampCommand(25,40,60,90,0.01,45))
        #self.addSequential(LeaveRampCommand(-25,-60,10,200,0.01,-20))
        #self.addSequential(TurnCommand(180))

        #start right to rocket3
        #self.addParallel(ZeroGyroCommand())
        #self.addSequential(LeaveRampCommand(0, 0, 0, 0, 0, 0))

        #start right to cargo1
        #self.addSequential(LeaveRampCommand(0,0,0,0,0,0))

        #start right to cargo2
        #self.addSequential(LeaveRampCommand(0,0,0,0,0,0))


        #vision move to tape
        #self.addSequential(visionmoveCommand())

        #backup and turn from rocket
        #self.addSequential(leaveRampCommand(-35,50,-24,35,.01,160))

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
