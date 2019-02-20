from wpilib.command.commandgroup import CommandGroup
import commandbased.flowcontrol as fc

from commands.climber.allextendcommand import AllExtendCommand
from commands.climber.frontretractcommand import FrontRetractCommand
from commands.climber.rearretractcommand import RearRetractCommand
from commands.climber.keeprearextendedcommand import KeepRearExtendedCommand
from commands.climber.getonplatformcommand import GetOnPlatformCommand
from commands.climber.driveforwardcommand import DriveForwardCommand

from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.setspeedcommand import SetSpeedCommand


class ClimbCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Climb')

        # Add commands here with self.addSequential() and self.addParallel()


        self.addSequential(AllExtendCommand())
        self.addSequential(GetOnPlatformCommand(), 3)
        self.addSequential(KeepRearExtendedCommand(), 3.5)
        self.addSequential(SetSpeedCommand(300))
        self.addSequential(DriveForwardCommand(), 4)
        self.addSequential(RearRetractCommand(), 3.5)
