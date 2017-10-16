from wpilib.command.commandgroup import CommandGroup
from wpilib.command.waitcommand import WaitCommand
import custom.flowcontrol as fc
import subsystems
from wpilib.command.printcommand import PrintCommand

from commands.gear.scoregearcommandgroup import ScoreGearCommandGroup
from commands.gear.waitonpilotcommand import WaitOnPilotCommand
from commands.drive.movecommand import MoveCommand
from wpilib.driverstation import DriverStation
from commands.drive.turncommand import TurnCommand
from commands.shooter.firecommand import FireCommand
from commands.setconfigcommand import SetConfigCommand
from commands.alterconfigcommand import AlterConfigCommand
from commands.gear.waitforliftcommand import WaitForLiftCommand
from custom.config import Config


class AutonomousCommandGroup(CommandGroup):
    def __init__(self):
        super().__init__('autonomous')
        ds = DriverStation.getInstance()

        '''Lined up with the boiler. Shoot some fuel.'''
        @fc.IF(lambda: subsystems.shooter.isVisible())
        def launchFuel(self):
            self.addSequential(FireCommand(Config('Shooter/speed')), 8)

            '''Get away from the wall'''
            @fc.IF(lambda: ds.getAlliance() == ds.Alliance.Red)
            def turnRight(self):
                self.addSequential(
                    SetConfigCommand('Autonomous/robotLocation', -60)
                )
                self.addSequential(MoveCommand(25))

                self.addSequential(WaitCommand(0.1))
                self.addSequential(TurnCommand(25))
                self.addSequential(MoveCommand(10))
                self.addSequential(WaitCommand(0.1))
                self.addSequential(TurnCommand(70))

            @fc.ELSE
            def turnLeft(self):
                self.addSequential(
                    SetConfigCommand('Autonomous/robotLocation', 60)
                )
                self.addSequential(MoveCommand(25))
                self.addSequential(WaitCommand(0.1))
                self.addSequential(TurnCommand(-25))
                self.addSequential(MoveCommand(10))
                self.addSequential(WaitCommand(0.1))
                self.addSequential(TurnCommand(-70))

            '''Hang a gear, if you got it. Otherwise just drive downfield'''
            @fc.IF(lambda: subsystems.gear.hasGear())
            def turnToLift(self):
                self.addSequential(MoveCommand(50))
                self.addSequential(
                    TurnCommand(Config('Autonomous/robotLocation'))
                )
                self.addSequential(WaitForLiftCommand())

            @fc.ELSE
            def goDownfield(self):
                self.addSequential(MoveCommand(300))

        '''We're starting on a side of the airship'''
        @fc.ELIF(lambda: not subsystems.gear.isLiftVisible())
        def offCenter(self):
            '''We know we're not in the center, so where are we?'''
            @fc.IF(lambda: Config('Autonomous/robotLocation') == 0)
            def guessPosition(self):
                @fc.IF(lambda: ds.getAlliance() == ds.Alliance.Red)
                def guessLeft(self):
                    self.addSequential(
                        SetConfigCommand('Autonomous/robotLocation', 60)
                    )
                @fc.ELSE
                def guessRight(self):
                    self.addSequential(
                        SetConfigCommand('Autonomous/robotLocation', -60)
                    )

            '''If a gear is loaded, hang it. Otherwise, drive downfield.'''
            @fc.IF(lambda: subsystems.gear.hasGear())
            def turnToLift(self):
                self.addSequential(MoveCommand(80))
                self.addSequential(
                    TurnCommand(Config('Autonomous/robotLocation'))
                )
                self.addSequential(WaitForLiftCommand(), 2)

                @fc.IF(lambda: not subsystems.gear.isLiftVisible())
                def doubleTurn(self):
                    self.addSequential(AlterConfigCommand(
                        'Autonomous/robotLocation',
                        lambda x: x * 2
                    ))

                @fc.WHILE(lambda: not subsystems.gear.isLiftVisible())
                def turnOtherWay(self):
                    self.addSequential(AlterConfigCommand(
                        'Autonomous/robotLocation',
                        lambda x: -x
                    ))
                    self.addSequential(WaitForLiftCommand(), 2)

            @fc.ELSE
            def goDownfield(self):
                self.addSequential(MoveCommand(300))

        @fc.ELSE
        def weAreCentered(self):
            self.addSequential(SetConfigCommand('Autonomous/robotLocation', 0))

            @fc.IF(lambda: not subsystems.gear.hasGear())
            def crossBaseline(self):
                self.addSequential(MoveCommand(50))

        '''If we've got a gear and can see a lift, do magic.'''
        @fc.IF(lambda:
            subsystems.gear.isLiftVisible() and subsystems.gear.hasGear()
        )
        def hangGear(self):
            self.addSequential(ScoreGearCommandGroup())
            self.addSequential(WaitOnPilotCommand(), 3)

            @fc.WHILE(lambda: subsystems.gear.hasGear())
            def retryHang(self):
                self.addSequential(MoveCommand(-40))
                self.addSequential(ScoreGearCommandGroup())
                self.addSequential(WaitOnPilotCommand(), 3)

            self.addSequential(MoveCommand(-10))

            @fc.IF(lambda: Config('Autonomous/robotLocation') == 0)
            def goDownfieldFromCenter(self):
                @fc.IF(lambda: ds.getAlliance() == ds.Alliance.Red)
                def turnLeft(self):
                    self.addSequential(TurnCommand(-90))
                    self.addSequential(MoveCommand(50))
                    self.addSequential(TurnCommand(90))

                @fc.ELSE
                def turnRight(self):
                    self.addSequential(TurnCommand(90))
                    self.addSequential(MoveCommand(50))
                    self.addSequential(TurnCommand(-90))

                self.addSequential(MoveCommand(240))

            @fc.ELSE
            def goDownfieldFromSide(self):
                self.addSequential(AlterConfigCommand(
                    'Autonomous/robotLocation',
                    lambda x: -x
                ))
                self.addSequential(
                    TurnCommand(Config('Autonomous/robotLocation'))
                )
                self.addSequential(MoveCommand(200))
