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
                self.addSequential(MoveWithGyroCommand(220))
                self.addParallel(IntakeCommand(), 10)
                self.addParallel(GoToHeightCommand('hang'))
                self.addSequential(SetSpeedCommand(1000))
                self.addSequential(PivotCommand(40), 2)
                self.addSequential(MoveWithGyroCommand(28))
                self.addSequential(OuttakeCommand(), 0.5)
                self.addParallel(GoToHeightCommand('ground'))
                self.addSequential(MoveWithGyroCommand(-28))

                #Switch
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(PivotCommand(135), 2)
                self.addParallel(IntakeCommand(), 10)
                self.addSequential(MoveWithGyroCommand(48))
                self.addSequential(GoToHeightCommand('switch'))
                self.addSequential(OuttakeCommand(), 0.5)
                self.addSequential(MoveWithGyroCommand(-10))
                self.addSequential(GoToHeightCommand('ground'))

            @fc.ELIF(getSwitch)
            def scoreSwitch(self):
                #1st cube
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(MoveWithGyroCommand(120))
                self.addSequential(SetSpeedCommand(2000))
                self.addParallel(IntakeCommand(), 10)
                self.addParallel(GoToHeightCommand('switch'))
                self.addSequential(PivotCommand(90), 2)
                self.addSequential(MoveWithGyroCommand(12), 3)
                self.addSequential(OuttakeCommand(), 0.5)
                self.addParallel(GoToHeightCommand('ground'))

                #2nd cube
                self.addSequential(PivotCommand(-95, True))
                self.addSequential(MoveWithGyroCommand(50))
                self.addSequential(PivotCommand(125), 2)
                self.addParallel(IntakeCommand(), 10)
                self.addSequential(MoveWithGyroCommand(10))
                self.addSequential(PivotCommand(90), 2)
                self.addParallel(IntakeCommand(), 10)
                self.addSequential(GoToHeightCommand('switch'))
                self.addSequential(MoveWithGyroCommand(5))
                self.addSequential(OuttakeCommand(), 0.5)

                '''
            def quickSwitch(self):
                #1st cube
                self.addSequential(SetSpeedCommand(2250))
                self.addParallel(GoToHeightCommand('switch'))
                self.addParallel(IntakeCommand(), 5)
                self.addSequential(MoveWithGyroCommand(95))
                self.addSequential(OuttakeCommand(), 0.5)
                self.addSequential(MoveWithGyroCommand(-10))
                self.addSequential(SetSpeedCommand(800))
                self.addSequential(GoToHeightCommand('ground'))

                #2nd Cube
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(PivotCommand(-90, True))
                self.addSequential(MoveWithGyroCommand(40))
                self.addSequential(PivotCommand(85), 2)
                self.addSequential(MoveWithGyroCommand(120))
                '''

            @fc.ELIF(lambda: Config('Autonomous/switch') == "always")
            def goToRightSwitch(self):
                #1st cube
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

                #2nd Cube
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(PivotCommand(90, True))
                self.addSequential(MoveWithGyroCommand(40))
                self.addSequential(PivotCommand(85), 2)
                self.addSequential(MoveWithGyroCommand(120))

            @fc.ELIF(getScale)
            def scoreScale(self):
                #1st cube
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(MoveWithGyroCommand(220))
                self.addParallel(IntakeCommand(), 10)
                self.addParallel(GoToHeightCommand('hang'))
                self.addSequential(SetSpeedCommand(1000))
                self.addSequential(PivotCommand(40), 2)
                self.addSequential(MoveWithGyroCommand(28))
                self.addSequential(OuttakeCommand(), 0.5)
                self.addParallel(GoToHeightCommand('ground'))
                self.addSequential(MoveWithGyroCommand(-28))

                #2nd cube
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(PivotCommand(135), 2)
                self.addParallel(IntakeCommand(), 10)
                self.addSequential(MoveWithGyroCommand(48))
                self.addSequential(MoveWithGyroCommand(-10))
                self.addSequential(TurnCommand(-90))
                self.addSequential(MoveWithGyroCommand(95))
                self.addSequential(TurnCommand(90))


            @fc.ELIF(lambda: Config('Autonomous/scale') == 'always')
            def goToRightScale(self):
                #Scale
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(MoveWithGyroCommand(190))
                self.addSequential(PivotCommand(90), 2)
                self.addSequential(MoveWithGyroCommand(192))
                self.addSequential(PivotCommand(-90), 2)
                self.addParallel(IntakeCommand(), 10)
                self.addParallel(GoToHeightCommand('hang'))
                self.addSequential(PivotCommand(-45), 2)
                self.addSequential(SetSpeedCommand(1000))
                self.addSequential(MoveWithGyroCommand(24))
                self.addSequential(OuttakeCommand(), 0.5)
                self.addSequential(SetSpeedCommand(1000))
                self.addParallel(GoToHeightCommand('ground'))
                self.addSequential(MoveWithGyroCommand(-28))

            @fc.ELSE
            def crossBaseline(self):
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(MoveWithGyroCommand(100))

        @fc.ELIF(lambda: Config('Autonomous/robotLocation') == 'R')
        def fromRight(self):

            @fc.IF(lambda: getScale() and getSwitch())
            def scaleAndSwitch(self):
                #Scale
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(MoveWithGyroCommand(220))
                self.addParallel(IntakeCommand(), 10)
                self.addParallel(GoToHeightCommand('hang'))
                self.addSequential(SetSpeedCommand(1000))
                self.addSequential(PivotCommand(-45), 2)
                self.addSequential(MoveWithGyroCommand(50))
                self.addSequential(OuttakeCommand(), 0.5)
                self.addParallel(GoToHeightCommand('ground'))
                self.addSequential(MoveWithGyroCommand(-28))

                #Switch
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(PivotCommand(-135), 2)
                self.addParallel(IntakeCommand(), 10)
                self.addSequential(MoveWithGyroCommand(48))
                self.addSequential(GoToHeightCommand('switch'))
                self.addSequential(OuttakeCommand(), 0.5)
                self.addSequential(MoveWithGyroCommand(-10))
                self.addSequential(GoToHeightCommand('ground'))

            @fc.ELIF(getSwitch)
            def scoreSwitch(self):
                #1st cube
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(MoveWithGyroCommand(120))
                self.addSequential(SetSpeedCommand(2000))
                self.addParallel(IntakeCommand(), 10)
                self.addParallel(GoToHeightCommand('switch'))
                self.addSequential(PivotCommand(-90), 2)
                self.addSequential(MoveWithGyroCommand(18), 3)
                self.addSequential(OuttakeCommand(), 0.5)
                self.addParallel(GoToHeightCommand('ground'))

                #2nd cube
                self.addSequential(PivotCommand(95, True))
                self.addSequential(MoveWithGyroCommand(50))
                self.addSequential(PivotCommand(-125), 2)
                self.addParallel(IntakeCommand(), 10)
                self.addSequential(MoveWithGyroCommand(10))
                self.addSequential(PivotCommand(-90), 2)
                self.addParallel(IntakeCommand(), 10)
                self.addSequential(GoToHeightCommand('switch'))
                self.addSequential(MoveWithGyroCommand(5))
                self.addSequential(OuttakeCommand(), 0.5)

                '''
            def quickSwitch(self):
                #1st cube
                self.addSequential(SetSpeedCommand(2250))
                self.addParallel(GoToHeightCommand('switch'))
                self.addParallel(IntakeCommand(), 5)
                self.addSequential(MoveWithGyroCommand(95))
                self.addSequential(OuttakeCommand(), 0.5)
                self.addSequential(MoveWithGyroCommand(-10))
                self.addSequential(SetSpeedCommand(800))
                self.addSequential(GoToHeightCommand('ground'))

                #2nd Cube
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(PivotCommand(90, True))
                self.addSequential(MoveWithGyroCommand(40))
                self.addSequential(PivotCommand(-85), 2)
                self.addSequential(MoveWithGyroCommand(120))
                '''

            @fc.ELIF(lambda: Config('Autonomous/switch') == 'always')
            def goToLeftSwitch(self):
                #1st cube
                self.addSequential(SetSpeedCommand(1500))
                self.addSequential(PivotCommand(-45), 2)
                self.addParallel(GoToHeightCommand('switch'))
                self.addParallel(IntakeCommand(), 10)
                self.addSequential(MoveWithGyroCommand(130))
                self.addSequential(PivotCommand(45), 2)
                self.addSequential(OuttakeCommand(), 0.5)
                self.addSequential(MoveWithGyroCommand(-10))
                self.addSequential(SetSpeedCommand(800))
                self.addSequential(GoToHeightCommand('ground'))

                #2nd Cube
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(PivotCommand(-90, True))
                self.addSequential(MoveWithGyroCommand(40))
                self.addSequential(PivotCommand(-85), 2)
                self.addSequential(MoveWithGyroCommand(120))

            @fc.ELIF(getScale)
            def scoreScale(self):
                #1st cube
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(MoveWithGyroCommand(220))
                self.addParallel(IntakeCommand(), 10)
                self.addParallel(GoToHeightCommand('hang'))
                self.addSequential(SetSpeedCommand(1000))
                self.addSequential(PivotCommand(-45), 2)
                self.addSequential(MoveWithGyroCommand(50))
                self.addSequential(OuttakeCommand(), 0.5)
                self.addParallel(GoToHeightCommand('ground'))
                self.addSequential(MoveWithGyroCommand(-28))

                #2nd cube
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(PivotCommand(-135), 2)
                self.addParallel(IntakeCommand(), 10)
                self.addSequential(MoveWithGyroCommand(48))
                self.addSequential(MoveWithGyroCommand(-10))
                self.addSequential(TurnCommand(90))
                self.addSequential(MoveWithGyroCommand(95))
                self.addSequential(TurnCommand(-90))


            @fc.ELIF(lambda: Config('Autonomous/scale') == 'always')
            def goToLeftScale(self):
                #Scale
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(MoveWithGyroCommand(190))
                self.addSequential(PivotCommand(-90), 2)
                self.addSequential(MoveWithGyroCommand(192))
                self.addSequential(PivotCommand(90), 2)
                self.addParallel(IntakeCommand(), 10)
                self.addParallel(GoToHeightCommand('hang'))
                self.addSequential(PivotCommand(45), 2)
                self.addSequential(SetSpeedCommand(1000))
                self.addSequential(MoveWithGyroCommand(24))
                self.addSequential(OuttakeCommand(), 0.5)
                self.addSequential(SetSpeedCommand(1000))
                self.addParallel(GoToHeightCommand('ground'))
                self.addSequential(MoveWithGyroCommand(-28))

            @fc.ELSE
            def crossBaseline(self):
                self.addSequential(SetSpeedCommand(2500))
                self.addSequential(MoveWithGyroCommand(100))

        @fc.ELSE
        def middle(self):

            @fc.IF(lambda: Config('Autonomous/switch') == 'always')
            def scoreSwitch(self):

                @fc.IF(lambda: ds.getGameSpecificMessage()[0] == 'L')
                def toLeft(self):
                    #1st cube
                    self.addSequential(SetSpeedCommand(2500))
                    self.addSequential(PivotCommand(-35), 2)
                    self.addSequential(SetSpeedCommand(2000))
                    self.addParallel(GoToHeightCommand('switch'))
                    self.addParallel(IntakeCommand(), 10)
                    self.addSequential(MoveWithGyroCommand(98), 3)
                    self.addSequential(PivotCommand(35), 2)
                    self.addSequential(OuttakeCommand(), 0.5)
                    self.addSequential(MoveWithGyroCommand(-10))
                    self.addParallel(GoToHeightCommand('ground'))

                    '''
                    #2nd Cube
                    self.addSequential(SetSpeedCommand(2500))
                    self.addSequential(PivotCommand(-90, True))
                    self.addSequential(MoveWithGyroCommand(55))
                    self.addSequential(PivotCommand(95), 2)
                    self.addSequential(MoveWithGyroCommand(76))
                    self.addSequential(PivotCommand(95), 2)
                    '''

                @fc.ELSE
                def toRight(self):
                    #1st cube
                    self.addSequential(SetSpeedCommand(2500))
                    self.addSequential(PivotCommand(27), 2)
                    self.addSequential(SetSpeedCommand(2000))
                    self.addParallel(GoToHeightCommand('switch'))
                    self.addParallel(IntakeCommand(), 10)
                    self.addSequential(MoveWithGyroCommand(100), 3)
                    self.addSequential(PivotCommand(-30), 2)
                    self.addSequential(OuttakeCommand(), 0.5)
                    self.addSequential(MoveWithGyroCommand(-10))
                    self.addParallel(GoToHeightCommand('ground'))

                    '''
                    #2nd cube
                    self.addSequential(SetSpeedCommand(2500))
                    self.addSequential(PivotCommand(90, True))
                    self.addSequential(MoveWithGyroCommand(55))
                    self.addSequential(PivotCommand(-95), 2)
                    self.addSequential(MoveWithGyroCommand(76))
                    self.addSequential(PivotCommand(-95), 2)
                    '''

            @fc.ELSE
            def crossBaselineCenter(self):
                @fc.IF(lambda: ds.getGameSpecificMessage()[0] == 'L')
                def crossLeft(self):
                    self.addSequential(SetSpeedCommand(2500))
                    self.addSequential(PivotCommand(-35), 2)
                    self.addSequential(MoveWithGyroCommand(98))
                    self.addSequential(PivotCommand(35), 2)

                @fc.ELSE
                def crossRight(self):
                    self.addSequential(SetSpeedCommand(2500))
                    self.addSequential(PivotCommand(30), 2)
                    self.addSequential(MoveWithGyroCommand(98))
                    self.addSequential(PivotCommand(-30), 2)


class ScoreOnSwitch(CommandGroup):
    def __init__(self):
        super().__init__('Score on switch')

        self.addSequential(OuttakeCommand(), 0.5)
        self.addSequential(MoveWithGyroCommand(-10))
        self.addSequential(SetSpeedCommand(800))
        self.addSequential(GoToHeightCommand('ground'))

class ScoreOnScale(CommandGroup):
    def __init__(self):
        super().__init__('Score on scale')

        self.addParallel(IntakeCommand(), 10)
        self.addSequential(GoToHeightCommand('hang'))
        self.addSequential(OuttakeCommand())
        self.addSequential(GoToHeightCommand('ground'))
