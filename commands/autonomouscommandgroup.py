from wpilib.command import CommandGroup
from wpilib.command import PrintCommand
from wpilib.driverstation import DriverStation
from custom.config import Config
from commands.network.alertcommand import AlertCommand
import commandbased.flowcontrol as fc

from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.pivotcommand import PivotCommand
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
            if Config('Autonomous/scale') == "always":
                return True
            if Config('Autonomous/scale') == "never":
                return False
            msg = ds.getGameSpecificMessage()[1]
            location = Config('Autonomous/robotLocation')
            return msg == location

        @fc.IF(lambda: Config('Autonomous/robotLocation') == 'L')
        def fromLeft(self):

            @fc.IF(getSwitch and getScale)
            def scaleAndSwitch(self):
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(GoToHeightCommand('portal'))
                self.addSequential(IntakeCommand())
                self.addSequential(MoveCommand(260))
                self.addSequential(PivotCommand(95))
                self.addSequential(ScoreOnScale())
                self.addSequential(GoToHeightCommand('ground'))
                #self.addSequential(GoToHeightCommand('switch'))
                #self.addSequential(ScoreOnSwitch))

            @fc.ELIF(getSwitch)
            def cubeOnSwitch(self):
                self.addSequential(SetSpeedCommand(1500))
                self.addParallel(GoToHeightCommand('portal'))
                self.addParallel(IntakeCommand())
                self.addSequential(MoveCommand(120))
                self.addSequential(PivotCommand(90))
                self.addParallel(ScoreOnSwitch())
                self.addSequential(MoveCommand(14))
                self.addSequential(MoveCommand(-5))
                self.addSequential(GoToHeightCommand('ground'))

            @fc.ELIF(lambda: Config('Autonomous/switch') == 'always')
            def goToRight(self):
                self.addSequential(SetSpeedCommand(1500))
                self.addSequential(GoToHeightCommand('portal'))
                self.addSequential(IntakeCommand())
                self.addSequential(MoveCommand(10))
                self.addSequential(PivotCommand(30))
                self.addSequential(MoveCommand(60))
                self.addSequential(PivotCommand(-30))
                self.addSequential(MoveCommand(10))
                self.addSequential(ScoreOnSwitch())
                self.addSequential(GoToHeightCommand('ground'))

            @fc.ELIF(getScale)
            def scoreScale(self):
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(GoToHeightCommand('portal'))
                self.addSequential(IntakeCommand())
                self.addSequential(MoveCommand(260))
                self.addSequential(PivotCommand(95))
                self.addSequential(ScoreOnScale())
                self.addSequential(GoToHeightCommand('ground'))

            @fc.ELSE
            def crossBaseline(self):
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(GoToHeightCommand('portal'))
                self.addSequential(IntakeCommand())
                self.addSequential(MoveCommand(100))

        @fc.ELIF(lambda: Config('Autonomous/robotLocation') == 'R')
        def fromRight(self):

            @fc.IF(getSwitch and getScale)
            def scaleAndSwitch(self):
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(GoToHeightCommand('portal'))
                self.addSequential(IntakeCommand())
                self.addSequential(MoveCommand(260))
                self.addSequential(PivotCommand(-95))
                self.addSequential(ScoreOnScale())
                self.addSequential(GoToHeightCommand('ground'))
                #self.addSequential(GoToHeightCommand('Switch'))
                #self.addSequential(ScoreOnSwitch))


            @fc.ELIF(getSwitch)
            def cubeOnSwitch(self):
                self.addSequential(SetSpeedCommand(1500))
                #self.addSequential(GoToHeightCommand('portal'))
                #self.addSequential(IntakeCommand())
                self.addSequential(MoveCommand(120))
                self.addSequential(PivotCommand(-95))
                self.addParallel(ScoreOnSwitch())
                self.addSequential(MoveCommand(14))
                self.addSequential(GoToHeightCommand('ground'))

            @fc.ELIF(lambda: Config('Autonomous/switch') == 'always')
            def goToLeft(self):
                self.addSequential(SetSpeedCommand(1500))
                self.addSequential(GoToHeightCommand('portal'))
                self.addSequential(IntakeCommand())
                self.addSequential(MoveCommand(10))
                self.addSequential(PivotCommand(-30))
                self.addSequential(MoveCommand(60))
                self.addSequential(PivotCommand(30))
                self.addSequential(MoveCommand(10))
                self.addSequential(ScoreOnSwitch())

            @fc.ELIF(getScale)
            def cubeOnScale(self):
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(GoToHeightCommand('portal'))
                self.addSequential(IntakeCommand())
                self.addSequential(MoveCommand(260))
                self.addSequential(PivotCommand(-95))
                self.addSequential(ScoreOnScale())

            @fc.ELSE
            def crossBaseline(self):
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(GoToHeightCommand('portal'))
                self.addSequential(IntakeCommand())
                self.addSequential(MoveCommand(88))

        @fc.ELSE
        def middle(self):
            @fc.IF(lambda: Config('Autonomous/switch') == 'always')
            def scoreSwitch(self):
                @fc.IF(lambda: ds.getGameSpecificMessage()[0] == 'L')
                def fromLeft(self):
                    self.addSequential(SetSpeedCommand(1500))
                    self.addSequential(GoToHeightCommand('portal'))
                    self.addSequential(IntakeCommand())
                    self.addSequential(PivotCommand(-40))
                    self.addSequential(MoveCommand(104))
                    self.addSequential(PivotCommand(40))
                    self.addSequential(ScoreOnSwitch())

                @fc.ELSE
                def fromRight(self):
                    self.addSequential(SetSpeedCommand(1500))
                    self.addSequential(GoToHeightCommand('portal'))
                    self.addSequential(IntakeCommand())
                    self.addSequential(PivotCommand(30))
                    self.addSequential(MoveCommand(92))
                    self.addSequential(PivotCommand(-30))
                    self.addSequential(ScoreOnSwitch())

            @fc.ELSE
            def crossBaselineCenter(self):
                @fc.IF(lambda: ds.getGameSpecificMessage()[0] == 'L')
                def crossRight(self):
                    self.addSequential(SetSpeedCommand(2500))
                    self.addSequential(GoToHeightCommand('portal'))
                    self.addSequential(IntakeCommand())
                    self.addSequential(MoveCommand(20))
                    self.addSequential(PivotCommand(45))
                    self.addSequential(MoveCommand(60))
                    self.addSequential(PivotCommand(-45))
                    self.addSequential(MoveCommand(20))
                    self.addSequential(ScoreOnSwitch())

                @fc.ELSE
                def crossLeft(self):
                    self.addSequential(SetSpeedCommand(2500))
                    self.addSequential(GoToHeightCommand('portal'))
                    self.addSequential(IntakeCommand())
                    self.addSequential(MoveCommand(20))
                    self.addSequential(PivotCommand(-45))
                    self.addSequential(MoveCommand(60))
                    self.addSequential(PivotCommand(45))
                    self.addSequential(MoveCommand(20))
                    self.addSequential(ScoreOnSwitch())


class ScoreOnSwitch(CommandGroup):
    def __init__(self):
        super().__init__('Score on switch')

        self.addSequential(GoToHeightCommand('switch'))
        self.addSequential(OuttakeCommand())
        self.addSequential(AlertCommand('We scored!', 'Info'))

class ScoreOnScale(CommandGroup):
    def __init__(self):
        super().__init__('Score on scale')

        self.addSequential(GoToHeightCommand('scale'))
        self.addSequential(OuttakeCommand())
        self.addSequential(AlertCommand('We scored!', 'Info'))
