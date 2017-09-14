from wpilib.command.commandgroup import CommandGroup
import custom.flowcontrol as fc
import subsystems
from commands.gear.scoregearcommandgroup import ScoreGearCommandGroup
from commands.gear.waitonpilotcommand import WaitOnPilotCommand
from commands.drive.movecommand import MoveCommand
from wpilib.driverstation import DriverStation
from commands.drive.turncommand import TurnCommand

class AutonomousCommandGroup(CommandGroup):
    def __init__(self):
        super().__init__('autonomous')

        @fc.IF(lambda: subsystems.gear.isLiftVisible())
        def centerPosition(self):
            @fc.IF(lambda: subsystems.gear.hasGear())
            def hangCenter(self):
                self.addSequential(ScoreGearCommandGroup())
                self.addSequential(WaitOnPilotCommand())
                self.addSequential(MoveCommand(-10))

                @fc.IF(lambda: DriverStation.getAlliance() == DriverStation.Alliance.Red)
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
            pass

        @fc.ELSE
        def sides(self):
            pass
