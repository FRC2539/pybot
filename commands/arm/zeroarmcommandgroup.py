from wpilib.command.commandgroup import CommandGroup
import commandbased.flowcontrol as fc

from commands.elevator.deelevatecommand import DeelevateCommand
from commands.arm.lowercommand import LowerCommand

class ZeroArmCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Zero Arm')

        # Add commands here with self.addSequential() and self.addParallel()

        #Make sure elevator is at end of travel.
        self.addSequential(DeelevateCommand())

        #Lower arm to end of travel.
        self.addSequential(LowerCommand())
