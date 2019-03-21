from wpilib.command.commandgroup import CommandGroup
import commandbased.flowcontrol as fc

from wpilib.command.waitcommand import WaitCommand

from commands.arm.lowercommand import LowerCommand
from commands.arm.downstagecommand import DownStageCommand
from commands.arm.upstagecommand import UpStageCommand

class SetArmCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Set Arm')

        # Add commands here with self.addSequential() and self.addParallel()
        self.addSequential(LowerCommand())
        self.addSequential(WaitCommand(0.5))
        self.addSequential(DownStageCommand())
        self.addSequential(UpStageCommand(20.0))
