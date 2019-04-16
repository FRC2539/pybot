from wpilib.command.commandgroup import CommandGroup
import commandbased.flowcontrol as fc

import robot

from commands.hatch.hatchintakecommand import HatchIntakeCommand
from commands.hatch.hatchejectcommand import HatchEjectCommand

from commands.drivetrain.gototapecommand import GoToTapeCommand
from commands.drivetrain.movecommand import MoveCommand


class GoToTapeCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Go To Tape')

        # Add commands here with self.addSequential() and self.addParallel()
        @fc.IF(lambda: not robot.hatch.hasHatchPanel())
        def grabHatch(self):
            self.addSequential(HatchIntakeCommand(), 8)

        self.addSequential(GoToTapeCommand())

        @fc.IF(lambda: robot.hatch.hasHatchPanel())
        def ejectHatch(self):
            self.addParallel(HatchEjectCommand())

        self.addSequential(MoveCommand(-12))
