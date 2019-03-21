from wpilib.command.commandgroup import CommandGroup
import commandbased.flowcontrol as fc

from wpilib.command.waitcommand import WaitCommand

from commands.elevator.deelevatecommand import DeelevateCommand

from commands.arm.lowercommand import LowerCommand
from commands.arm.downstagecommand import DownStageCommand
from commands.arm.upstagecommand import UpStageCommand

class SetArmCommandGroup(CommandGroup):

    def __init__(self, target):
        super().__init__('Set Arm')

        # Add commands here with self.addSequential() and self.addParallel()

        #Make sure elevator is at end of travel.
        self.addSequential(DeelevateCommand())

        #Lower arm to end of travel.
        self.addSequential(LowerCommand())

        #Wait for ramp rate to finish up.
        self.addSequential(WaitCommand(0.5))

        #Make sure arm is at correct zero position.
        self.addSequential(DownStageCommand())

        #Move arm to desired position.
        self.addSequential(UpStageCommand(float(target)))
