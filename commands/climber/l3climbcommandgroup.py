from wpilib.command.commandgroup import CommandGroup
import commandbased.flowcontrol as fc

from commands.climber.allextendcommand import AllExtendCommand
from commands.climber.rearretractcommand import RearRetractCommand
from commands.climber.keeprearextendedcommand import KeepRearExtendedCommand
from commands.climber.getonplatformcommand import GetOnPlatformCommand
from commands.climber.driveforwardcommand import DriveForwardCommand
from commands.lights.seizurelightscommand import SeizureLightsCommand


class L3ClimbCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Climb')

        # Add commands here with self.addSequential() and self.addParallel()

        #Lift robot up.
        self.addSequential(AllExtendCommand(), 5)

        #Get front wheels on platform.
        self.addSequential(GetOnPlatformCommand(), 2)

        #Front racks up.
        self.addSequential(KeepRearExtendedCommand(), 1.75)

        #Get back wheels on.
        self.addSequential(DriveForwardCommand(), 2)

        #Rear rack up.
        self.addSequential(RearRetractCommand(), 1.75)

        #Turn on Seizure Lights
        self.addSequential(SeizureLightsCommand())
