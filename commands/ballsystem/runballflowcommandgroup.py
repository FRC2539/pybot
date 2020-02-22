from wpilib.command import CommandGroup
import commandbased.flowcontrol as fc

from commands.ballsystem.runallcommand import RunAllCommand
from commands.intake.intakecommand import IntakeCommand

class RunBallFlowCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Run Ball Flow')

        # Add commands here with self.addSequential() and self.addParallel()
        self.addParallel(RunAllCommand())
        self.addParallel(IntakeCommand(0.3))
