from wpilib.command.commandgroup import CommandGroup
import commandbased.flowcontrol as fc

from commands.climber.allextendcommand import AllExtendCommand
from commands.climber.rearretractcommand import RearRetractCommand
from commands.climber.keeprearextendedcommand import KeepRearExtendedCommand
from commands.climber.getonplatformcommand import GetOnPlatformCommand
from commands.climber.driveforwardcommand import DriveForwardCommand
from commands.lights.seizurelightscommand import SeizureLightsCommand

from commands.drivetrain.setspeedcommand import SetSpeedCommand
from commands.drivetrain.movecommand import MoveCommand

class L3ClimbCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Climb')

        # Add commands here with self.addSequential() and self.addParallel()

        #Lift robot up.
        self.addSequential(AllExtendCommand())

        #Get front wheels on platform.
        self.addSequential(GetOnPlatformCommand(), 2)

        #Front racks up.
        self.addSequential(KeepRearExtendedCommand(), 1.75)

        #Get back wheels on.
        self.addSequential(DriveForwardCommand(), 3)

        #Rear rack up.
        self.addSequential(RearRetractCommand(), 1.75)

        #Set lower speed.
        #self.addSequential(SetSpeedCommand(800))

        #Move in
        #self.addSequential(MoveCommand(6))

        #Turn on Seizure Lights
        self.addSequential(SeizureLightsCommand())
