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
from custom.config import Config


class AutonomousCommandGroup(CommandGroup):
    def __init__(self):
        super().__init__('autonomous')
        ds = DriverStation.getInstance()

        @fc.IF(lambda: subsystems.gear.isLiftVisible())
        def centerPosition(self):
            @fc.IF(lambda: subsystems.gear.hasGear())
            def hangCenter(self):
                self.addSequential(ScoreGearCommandGroup())
                self.addSequential(WaitOnPilotCommand())
                self.addSequential(MoveCommand(-10))

                @fc.IF(lambda: ds.getAlliance() == ds.Alliance.Red)
                def turnLeft(self):
                    self.addSequential(TurnCommand(-90))
                    self.addSequential(MoveCommand(50))
                    self.addSequential(TurnCommand(90))
                    self.addSequential(MoveCommand(240))

                @fc.ELSE
                def turnRight(self):
                    self.addSequential(TurnCommand(90))
                    self.addSequential(MoveCommand(50))
                    self.addSequential(TurnCommand(-90))
                    self.addSequential(MoveCommand(240))

            @fc.ELSE
            def crossBaseline(self):
                self.addSequential(MoveCommand(50))

        @fc.ELIF(lambda: subsystems.shooter.isVisible())
        def shootingFuel(self):
            self.addSequential(FireCommand(Config('Shooter/speed')), 8)

            @fc.IF(lambda: ds.getAlliance() == ds.Alliance.Red)
            def turnRight(self):
                self.addSequential(MoveCommand(25))

                self.addSequential(WaitCommand(0.1))
                self.addSequential(PrintCommand('Hi'))
                self.addSequential(TurnCommand(25))
                self.addSequential(PrintCommand('Hi Again'))
                self.addSequential(MoveCommand(10))
                self.addSequential(WaitCommand(0.1))
                self.addSequential(TurnCommand(70))

            @fc.ELSE
            def turnLeft(self):
                self.addSequential(MoveCommand(-25))
                self.addSequential(WaitCommand(0.1))
                self.addSequential(TurnCommand(-25))
                self.addSequential(MoveCommand(-10))
                self.addSequential(WaitCommand(0.1))
                self.addSequential(TurnCommand(-70))

            @fc.IF(lambda: subsystems.gear.isLiftVisible())
            def centerPosition(self):
                @fc.IF(lambda: subsystems.gear.hasGear())
                def hangCenter(self):
                    self.addSequential(ScoreGearCommandGroup())
                    self.addSequential(WaitOnPilotCommand())
                    self.addSequential(MoveCommand(-10))

                @fc.IF(lambda: ds.getAlliance() == ds.Alliance.Red)
                def turnLeft(self):
                    self.addSequential(TurnCommand(-90))
                    self.addSequential(MoveCommand(50))
                    self.addSequential(TurnCommand(90))
                    self.addSequential(MoveCommand(240))

                @fc.ELSE
                def turnRight(self):
                    self.addSequential(TurnCommand(90))
                    self.addSequential(MoveCommand(50))
                    self.addSequential(TurnCommand(-90))
                    self.addSequential(MoveCommand(240))


        @fc.ELSE
        def sides(self):
            pass
