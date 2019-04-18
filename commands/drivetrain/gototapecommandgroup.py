from wpilib.command.commandgroup import CommandGroup
import commandbased.flowcontrol as fc

import robot

from commands.hatch.hatchintakecommand import HatchIntakeCommand
from commands.hatch.hatchejectcommand import HatchEjectCommand
from commands.hatch.defaultcommand import DefaultCommand

from commands.drivetrain.gototapecommand import GoToTapeCommand
from commands.drivetrain.gopasttapecommand import GoPastTapeCommand
from commands.drivetrain.movecommand import MoveCommand


class GoToTapeCommandGroup(CommandGroup):

    def __init__(self, pipeline=1):
        super().__init__('Go To Tape')

        # Add commands here with self.addSequential() and self.addParallel()
        @fc.IF(lambda: not robot.hatch.hasHatchPanel())
        def grabHatch(self):
            self.addParallel(HatchIntakeCommand())
            self.addSequential(GoToTapeCommand(pipeline))
            self.addParallel(HatchIntakeCommand(True), 3)
            self.addSequential(GoPastTapeCommand(), 1)
            #self.addParallel(DefaultCommand())
            self.addSequential(MoveCommand(-12))

        @fc.IF(lambda: robot.hatch.hasHatchPanel())
        def placeHatch(self):
            self.addSequential(GoToTapeCommand(pipeline))
            self.addSequential(GoPastTapeCommand(), 1)
            self.addParallel(HatchEjectCommand())
            self.addSequential(MoveCommand(-12))
