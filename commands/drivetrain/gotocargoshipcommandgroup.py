from wpilib.command.commandgroup import CommandGroup
import commandbased.flowcontrol as fc

from commands.drivetrain.gotocargoshipcommand import GoToCargoshipCommand
from commands.drivetrain.transitionmovecommand import TransitionMoveCommand

from commands.hatch.hatchejectcommand import HatchEjectCommand

class GoToCargoshipCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Go To Cargoship')
        self.addSequential(GoToCargoshipCommand(), 4.5)
        self.addParallel(HatchEjectCommand(), 0.5)
        self.addSequential(TransitionMoveCommand(-100,-100,-12,-12,0,0))

        # Add commands here with self.addSequential() and self.addParallel()
