from wpilib.command import CommandGroup
from wpilib.command import PrintCommand
from wpilib.driverstation import DriverStation
from custom.config import Config
from commands.network.alertcommand import AlertCommand
from wpilib.command.waitcommand import WaitCommand
import commandbased.flowcontrol as fc

from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.pivotcommand import PivotCommand
from commands.drivetrain.turncommand import TurnCommand
from commands.drivetrain.runintowallcommand import RunIntoWallCommand
from commands.drivetrain.setspeedcommand import SetSpeedCommand
from commands.drivetrain.gotowallcommand import GoToWallCommand
from commands.elevator.gotoheightcommand import GoToHeightCommand
from commands.intake.intakecommand import IntakeCommand
from commands.intake.outtakecommand import OuttakeCommand

class AutonomousCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Autonomous')

        ds = DriverStation.getInstance()

        def getSwitch():
            if Config('Autonomous/switch') == "never":
                return False

            msg = ds.getGameSpecificMessage()[0]
            location = Config('Autonomous/robotLocation')
            return msg == location

        def getScale():
            if Config('Autonomous/scale') == "never":
                return False

            msg = ds.getGameSpecificMessage()[1]
            location = Config('Autonomous/robotLocation')
            return msg == location


        @fc.IF(lambda: Config('Autonomous/robotLocation') == 'L')
        def fromLeft(self):

            @fc.IF(lambda: getScale() and getSwitch())
            def scaleAndSwitch(self):
                #Scale
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(MoveCommand(220))
                self.addParallel(IntakeCommand(), 10)
                self.addParallel(GoToHeightCommand('hang'))
                self.addSequential(SetSpeedCommand(1000))
                self.addSequential(PivotCommand(45))
                self.addSequential(MoveCommand(32))
                self.addSequential(OuttakeCommand(), 0.5)
                self.addParallel(GoToHeightCommand('ground'))
                self.addSequential(MoveCommand(-12))

                #Switch
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(PivotCommand(126))
                self.addParallel(IntakeCommand(), 10)
                self.addSequential(MoveCommand(60))
                self.addSequential(GoToHeightCommand('portal'))
                self.addSequential(OuttakeCommand(), 0.5)
                self.addSequential(ScoreOnSwitch())

            @fc.ELIF(getSwitch)
            def scoreSwitch(self):
                self.addSequential(SetSpeedCommand(2000))
                self.addSequential(MoveCommand(120))
                self.addParallel(IntakeCommand(), 5)
                self.addParallel(GoToHeightCommand('switch'))
                self.addSequential(PivotCommand(95))
                self.addSequential(MoveCommand(16))
                self.addSequential(ScoreOnSwitch())

                '''
                @fc.ELIF
                def quickSwitch(self):
                    self.addSequential(SetSpeedCommand(2250))
                    self.addParallel(GoToHeightCommand('switch'))
                    self.addParallel(IntakeCommand(), 5)
                    self.addSequential(MoveCommand(95))
                    self.addSequential(ScoreOnSwitch())
                '''

            @fc.ELIF(lambda: Config('Autonomous/switch') == "always")
            def goToRightSwitch(self):
                self.addSequential(SetSpeedCommand(1500))
                self.addSequential(PivotCommand(45))
                self.addParallel(GoToHeightCommand('portal'))
                self.addParallel(IntakeCommand())
                self.addSequential(MoveCommand(130))
                self.addSequential(PivotCommand(-45))
                self.addSequential(ScoreOnSwitch())

            @fc.ELIF(getScale)
            def scoreScale(self):
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(MoveCommand(220))
                self.addParallel(IntakeCommand(), 10)
                self.addParallel(GoToHeightCommand('hang'))
                self.addSequential(SetSpeedCommand(450))
                self.addSequential(PivotCommand(45))
                self.addSequential(MoveCommand(32))
                self.addSequential(OuttakeCommand(), 0.5)
                self.addParallel(GoToHeightCommand('ground'))
                self.addSequential(MoveCommand(-12))

            @fc.ELIF(lambda: Config('Autonomous/scale') == 'always')
            def goToRightScale(self):
                self.addSequential(SetSpeedCommand(1500))
                self.addSequential(MoveCommand(200))
                self.addSequential(PivotCommand(95))
                self.addSequential(MoveCommand(150))
                #self.addSequential(PivotCommand(-90))
                #self.addSequential(MoveCommand(20))
                #self.addSequential(PivotCommand(-45))
                #self.addParallel(IntakeCommand(), 10)
                #self.addParallel(GoToHeightCommand('hang'))
                #self.addSequential(SetSpeedCommand(450))
                #self.addSequential(PivotCommand(45))
                #self.addSequential(MoveCommand(32))
                #self.addSequential(OuttakeCommand(), 0.5)
                #self.addParallel(GoToHeightCommand('ground'))
                #self.addSequential(MoveCommand(-12))

            @fc.ELSE
            def crossBaseline(self):
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(MoveCommand(100))

        @fc.ELIF(lambda: Config('Autonomous/robotLocation') == 'R')
        def fromRight(self):

            @fc.IF(lambda: getScale() and getSwitch())
            def scaleAndSwitch(self):
                #Scale
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(MoveCommand(220))
                self.addParallel(IntakeCommand(), 10)
                self.addParallel(GoToHeightCommand('hang'))
                self.addSequential(SetSpeedCommand(450))
                self.addSequential(PivotCommand(-45))
                self.addSequential(MoveCommand(32))
                self.addSequential(OuttakeCommand(), 0.5)
                self.addParallel(GoToHeightCommand('ground'))
                self.addSequential(MoveCommand(-12))

                #Switch
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(PivotCommand(-126))
                self.addParallel(IntakeCommand(), 10)
                self.addSequential(MoveCommand(60))
                self.addSequential(GoToHeightCommand('switch'))
                self.addSequential(OuttakeCommand(), 0.5)
                self.addSequential(ScoreOnSwitch())

            @fc.ELIF(getSwitch)
            def scoreSwitch(self):
                self.addSequential(SetSpeedCommand(2250))
                self.addParallel(IntakeCommand(), 5)
                self.addParallel(GoToHeightCommand('switch'))
                self.addSequential(MoveCommand(120))
                self.addSequential(PivotCommand(-95))
                self.addSequential(MoveCommand(16))
                self.addSequential(ScoreOnSwitch())

                '''
                @fc.ELSE
                def quickSwitch(self):
                    self.addSequential(SetSpeedCommand(2250))
                    self.addParallel(GoToHeightCommand('switch'))
                    self.addParallel(IntakeCommand(), 5)
                    self.addSequential(MoveCommand(95))
                    self.addSequential(PrintCommand('start'))
                    self.addSequential(ScoreOnSwitch())
                '''

            @fc.ELIF(lambda: Config('Autonomous/switch') == 'always')
            def goToLeftSwitch(self):
                self.addSequential(SetSpeedCommand(1500))
                self.addSequential(PivotCommand(-60))
                #self.addParallel(GoToHeightCommand('portal'))
                #self.addParallel(IntakeCommand())
                self.addSequential(MoveCommand(120))
                self.addSequential(PivotCommand(60))
                self.addSequential(ScoreOnSwitch())

            @fc.ELIF(getScale)
            def scoreScale(self):
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(MoveCommand(220))
                self.addParallel(IntakeCommand(), 10)
                self.addParallel(GoToHeightCommand('hang'))
                self.addSequential(SetSpeedCommand(450))
                self.addSequential(PivotCommand(-45))
                self.addSequential(MoveCommand(32))
                self.addSequential(OuttakeCommand(), 0.5)
                self.addParallel(GoToHeightCommand('ground'))
                self.addSequential(MoveCommand(-12))

            @fc.ELIF(lambda: Config('Autonomous/scale') == 'always')
            def goToLeftScale(self):
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(MoveCommand(220))
                self.addParallel(IntakeCommand(), 10)
                self.addParallel(GoToHeightCommand('hang'))
                self.addSequential(SetSpeedCommand(450))
                self.addSequential(PivotCommand(-45))
                self.addSequential(MoveCommand(32))
                self.addSequential(OuttakeCommand(), 0.5)
                self.addParallel(GoToHeightCommand('ground'))

            @fc.ELSE
            def crossBaseline(self):
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(MoveCommand(100))

        @fc.ELSE
        def middle(self):

            @fc.IF(lambda: Config('Autonomous/switch') == 'always')
            def scoreSwitch(self):

                @fc.IF(lambda: ds.getGameSpecificMessage()[0] == 'L')
                def toLeft(self):
                    self.addSequential(SetSpeedCommand(2500))
                    self.addSequential(PivotCommand(-35))
                    self.addSequential(SetSpeedCommand(2000))
                    self.addParallel(GoToHeightCommand('portal'))
                    self.addParallel(IntakeCommand(), 8)
                    self.addSequential(MoveCommand(98))
                    self.addSequential(PivotCommand(35))
                    self.addSequential(OuttakeCommand(), 0.5)
                    self.addSequential(MoveCommand(-10))
                    self.addParallel(GoToHeightCommand('ground'))
                    self.addSequential(SetSpeedCommand(2500))
                    self.addSequential(PivotCommand(-90, True))
                    self.addSequential(MoveCommand(40))
                    self.addSequential(PivotCommand(85))
                    self.addSequential(MoveCommand(120))

                @fc.ELSE
                def toRight(self):
                    self.addSequential(SetSpeedCommand(2500))
                    self.addSequential(PivotCommand(30))
                    self.addSequential(SetSpeedCommand(2000))
                    self.addParallel(GoToHeightCommand('portal'))
                    self.addParallel(IntakeCommand(), 8)
                    self.addSequential(MoveCommand(98))
                    self.addSequential(PivotCommand(-30))
                    self.addSequential(OuttakeCommand(), 0.5)
                    self.addSequential(MoveCommand(-10))
                    self.addParallel(GoToHeightCommand('ground'))
                    self.addSequential(SetSpeedCommand(2500))
                    self.addSequential(PivotCommand(90, True))
                    #self.addSequential(MoveCommand(40))
                    #self.addSequential(PivotCommand(-85))
                    #self.addSequential(MoveCommand(120))


            @fc.ELSE
            def crossBaselineCenter(self):
                @fc.IF(lambda: ds.getGameSpecificMessage()[0] == 'L')
                def crossLeft(self):
                    self.addSequential(SetSpeedCommand(2500))
                    self.addSequential(MoveCommand(20))
                    self.addSequential(PivotCommand(-45))
                    self.addSequential(MoveCommand(60))
                    self.addSequential(PivotCommand(45))
                    self.addSequential(MoveCommand(10))

                @fc.ELSE
                def crossRight(self):
                    self.addSequential(SetSpeedCommand(2500))
                    self.addSequential(MoveCommand(20))
                    self.addSequential(PivotCommand(45))
                    self.addSequential(MoveCommand(60))
                    self.addSequential(PivotCommand(-45))
                    self.addSequential(MoveCommand(10))

class ScoreOnSwitch(CommandGroup):
    def __init__(self):
        super().__init__('Score on switch')

        self.addSequential(OuttakeCommand(), 0.5)
        self.addSequential(MoveCommand(-10))
        self.addSequential(SetSpeedCommand(800))
        self.addSequential(GoToHeightCommand('ground'))

class ScoreOnScale(CommandGroup):
    def __init__(self):
        super().__init__('Score on scale')

        self.addParallel(IntakeCommand(), 10)
        self.addSequential(GoToHeightCommand('hang'))
        self.addSequential(OuttakeCommand())
        self.addSequential(GoToHeightCommand('ground'))
