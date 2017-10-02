from wpilib.command.commandgroup import CommandGroup
import custom.flowcontrol as fc
import subsystems
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
                self.addSequential(MoveCommand(-20))
                self.addSequential(TurnCommand(10))
                self.addSequential(MoveCommand(5))
                self.addSequential(TurnCommand(20))
                self.addSequential(MoveCommand(5))
                self.addSequential(TurnCommand(20))
                self.addSequential(MoveCommand(20))
                self.addSequential(TurnCommand(-90))
                self.addSequential(MoveCommand(25))

            @fc.ELSE
            def turnLeft(self):
                self.addSequential(MoveCommand(10))
                self.addSequential(TurnCommand(-90))
                self.addSequential(MoveCommand(15))
                self.addSequential(TurnCommand(90))

        @fc.ELSE
        def sides(self):
            pass
