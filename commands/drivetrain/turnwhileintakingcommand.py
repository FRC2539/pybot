from wpilib.command import CommandGroup, WaitCommand

from commands.intake.lowerintakecommand import LowerIntakeCommand
from commands.drivetrain.manageballsmovecommand import ManageBallsMoveCommand

class TurnWhileIntakingCommandGroup(CommandGroup):
    def __init__(self, distance):
        super().__init__("Move While Intaking Command Group")

        self.addParallel(LowerIntakeCommand())
        self.addSequential(WaitCommand(1))
        self.addSequential(ManageBallsMoveCommand(distance))    
