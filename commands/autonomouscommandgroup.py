from wpilib.command import CommandGroup
from wpilib.command import PrintCommand
from wpilib.driverstation import DriverStation
from custom.config import Config
from commands.network.alertcommand import AlertCommand
from wpilib.command.waitcommand import WaitCommand
import commandbased.flowcontrol as fc

from networktables import NetworkTables

#from commands.drivetrain.movecommand import MoveCommand
#from commands.drivetrain.movewithgyrocommand import MoveWithGyroCommand
#from commands.drivetrain.pivotcommand import PivotCommand
#from commands.drivetrain.turncommand import TurnCommand
#from commands.drivetrain.runintowallcommand import RunIntoWallCommand
#from commands.drivetrain.setspeedcommand import SetSpeedCommand
#from commands.drivetrain.gotowallcommand import GoToWallCommand
#from commands.elevator.gotoheightcommand import GoToHeightCommand
#from commands.intake.intakecommand import IntakeCommand
#from commands.intake.outtakecommand import OuttakeCommand
#from commands.intake.slowouttakecommand import SlowOuttakeCommand

from commands.drivetrain.movewithgyrocommand import MoveWithGyroCommand
from commands.drivetrain.zerogyrocommand import ZeroGyroCommand
#from commands.drivetrain.newrampingspeedcommand import NewRampingSpeedCommand
from commands.drivetrain.visionmovecommand import VisionMoveCommand
from commands.drivetrain.transitionmovecommand import TransitionMoveCommand

from commands.drivetrain.movewithgyrocommand import MoveWithGyroCommand
from commands.drivetrain.turncommand import TurnCommand
from commands.drivetrain.pivotcommand import PivotCommand
from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.setspeedcommand import SetSpeedCommand

from commands.intake.slowejectcommand import SlowEjectCommand

from commands.superstructure.superstructuregotolevelcommand import SuperStructureGoToLevelCommand



class AutonomousCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Autonomous')

        NetworkTables.initialize(server='10.25.39.2')

        ds = DriverStation.getInstance()

        #self.addSequential(SetSpeedCommand(2500))
        dt = NetworkTables.getTable('DriveTrain')
        dt.putNumber('ticksPerInch', 300)
        dt.putNumber('DriveTrain/width', 200)
        #dt.putNumber('DriveTrain/width', 350)
        #dt.putNumber('DriveTrain/width', 350)
        #dt.putNumber('DriveTrain/width', 350)
        #dt.putNumber('DriveTrain/width', 350)
        #dt.putNumber('DriveTrain/width', 350)
        #dt.putNumber('DriveTrain/width', 350)
        dt.putNumber('normalSpeed', 2500)
        dt.putNumber('maxSpeed', 2500)

        Config('DriveTrain/ticksPerInch', 350)
        Config('DriveTrain/width', 29.5)
        Config('DriveTrain/Speed/P', 1)
        Config('DriveTrain/Speed/IZone', 30)
        Config('DriveTrain/Speed/D', 31)
        Config('DriveTrain/Speed/I', 0.001)
        Config('DriveTrain/Speed/F', 0.7)
        Config('DriveTrain/normalSpeed', 2500)
        Config('DriveTrain/maxSpeed', 2500)

        print('dtms: '+str(Config('DriveTrain/maxSpeed', '')))
        print('citf: '+str(Config('CameraInfo/tapeFound', '')))
        print('ac: '+str(Config('Autonomous/autoModeSelect', '')))
        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect', '')) == '1')
        def rrfAuto(self):
            #RightRocketFRont
            self.addSequential(TransitionMoveCommand(30,80,20,80,10,40))
            ##self.addSequential(VisionMoveCommand())
            ##self.addSequential(TransitionMoveCommand(-50,60,-60,220,1,145))

        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect', '')) == '2')
        def rrbAuto(self):
            #RightRocketback
            self.addSequential(TransitionMoveCommand(30,60,30,160,50,15))
            self.addSequential(TurnCommand(250))
            ##self.addSequential(VisionMoveCommand())
            ##self.addSequential(TransitionMoveCommand(60,60,5,115,10,150))
            ##self.addSequential(VisionMoveCommand())

        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect', '')) == '3')
        def rcfAuto(self):
            #RightCaRgoFRont

            self.addSequential(SetSpeedCommand(800))
            self.addSequential(TransitionMoveCommand(30, 50, 20, 30, 0, 0))
            self.addSequential(SuperStructureGoToLevelCommand('lowHatches'))


            #self.addSequential(TransitionMoveCommand(30,60,20,80,1,-30))
            ##self.addSequential(VisionMoveCommand())
            ##self.addSequential(SlowEjectCommand(), 1)
            ##self.addSequential(TurnCommand(-160))
            ##self.addSequential(TransitionMoveCommand(30,60,30,270,140,-50))
            ##self.addSequential(VisionMoveCommand())

        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect', '')) == '4')
        def lrfAuto(self):
            #LeftRocketFRont
            self.addSequential(TransitionMoveCommand(30,80,20,80,10,-40))
            ##self.addSequential(VisionMoveCommand())
            ##self.addSequential(TransitionMoveCommand(-50,60,-60,220,1,145))

        @fc.IF(lambda: str(Config('Autonomous/autoModeSelect', '')) == '5')
        def lrbAuto(self):
            #LeftRocketback
            self.addSequential(TransitionMoveCommand(30,60,30,160,50,-15))
            self.addSequential(TurnCommand(-250))
            ##self.addSequential(VisionMoveCommand())
            ##self.addSequential(TransitionMoveCommand(60,60,5,115,10,150))
            ##self.addSequential(VisionMoveCommand())

        #leftCaRgoFRont


        #leftRocketfront

        #leftRocketFRont



        #self.addSequential(VisionMoveCommand())

        #self.addSequential(VisionMoveCommand())
        #self.addParallel(SuperStructureGoToLevelCommand('midHatches'))


        #self.addParallel(SuperStructureGoToLevelCommand('lowHatches'))

        #self.addSequential(MoveCommand(100))
        #Config('DriveTrain/ticksPerInch', 350)
        #


        #self.addSequential(TransitionMoveCommand(30,60,30,100,0,0))

        ###visionmove demo
        #self.addSequential(VisionMoveCommand())

        #@fc.IF(lambda: Config('Autonomous/Auto', '') == 'RightRocketFront')
        #def rightFrontAuto(self):
        #cargoship to place first hatch then go to ham play place
        #self.addSequential(TransitionMoveCommand(30,60,30,200,1,-30))
        #self.addSequential(VisionMoveCommand())
        #self.addSequential(SlowEjectCommand(), 1)
        #self.addSequential(TurnCommand(-160))
        #self.addSequential(TransitionMoveCommand(30,60,30,270,140,-50))
        #self.addSequential(VisionMoveCommand())


        #@fc.IF(lambda: Config('Autonomous/Auto', '') == 'RightRocketBack')
        #def rightBackAuto(self):
        #start right to rocket3
        #self.addSequential(TransitionMoveCommand(30,60,30,260,50,15))
        #self.addSequential(TurnCommand(250))
        #self.addSequential(VisionMoveCommand())
        #self.addSequential(TransitionMoveCommand(60,60,5,115,10,150))
        #self.addSequential(VisionMoveCommand())

        '''
        @fc.IF(lambda: Config('Autonomous/Auto') == '1')
        def rightAuto(self):
            ###go to rocket then go to ham play place
            self.addSequential(TransitionMoveCommand(30,60,30,220,1,45))
            #self.addSequential(VisionMoveCommand())
            self.addSequential(TransitionMoveCommand(-50,60,-60,220,1,145))

        @fc.IF(lambda: Config('Autonomous/Auto') == '1')
        def centerauto(self):
            ###cargoship to place first hatch then go to ham play place
            self.addSequential(TransitionMoveCommand(30,60,30,240,1,-30))
            self.addSequential(TurnCommand(160))
            self.addSequential(TransitionMoveCommand(30,60,30,270,140,50))
            self.addSequential(VisionMoveCommand())
        '''





        #slowspeed,highspeed,transitionDistance,endDistance,rotateDistance=0,degrees=0
        #rotateDistance must be higher than transitionDistance for it to continue moving after the rotation.
        #if rotatedistance is above 30, it moves until it hits the wall. IF rotateDistance is below 30, it moves the same small distance every time.
        #we have no control over when it turn

        #start right to rocket1
        #self.addSequential(TransitionMoveCommand(30,80,30,155,5,50))
        #self.addSequential(VisionMoveCommand())
        #self.addSequential(TransitionMoveCommand(-35,80,-30,83,0.1,190))
        #self.addSequential(VisionMoveCommand())

        #start right to rocket2
        #self.addSequential(TransitionMoveCommand(30,50,30,100,85,75))
        #self.addSequential(VisionMoveCommand())
        #self.addSequential(TransitionMoveCommand(-35,50,-24,83,0.1,55))

        #start right to rocket3
        #self.addSequential(TransitionMoveCommand(30,80,30,250,200,100))
        #self.addSequential(VisionMoveCommand())
        #self.addSequential(TransitionMoveCommand(0,0,0,0,0,0))

        #start right to cargo1
        #self.addSequential(TransitionMoveCommand(0,0,0,0,0,0))

        #start right to cargo2
        #self.addSequential(TransitionMoveCommand(0,0,0,0,0,0))


        #vision move to tape
        #self.addSequential(VisionMoveCommand())

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
