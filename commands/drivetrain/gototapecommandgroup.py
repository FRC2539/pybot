from wpilib.command.commandgroup import CommandGroup
import commandbased.flowcontrol as fc

import robot

from commands.lights.seizurelightscommand import SeizureLightsCommand

from commands.drivetrain.gototapecommand import GoToTapeCommand
from commands.drivetrain.gopasttapecommand import GoPastTapeCommand
from commands.drivetrain.transitionmovecommand import TransitionMoveCommand
from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.timedmovecommand import TimedMoveCommand
from commands.hatch.hatchejectcommand import HatchEjectCommand
from commands.hatch.hatchintakecommand import HatchIntakeCommand

from commands.lights.seizurelightscommand import SeizureLightsCommand

from commands.resetcommand import ResetCommand


class GoToTapeCommandGroup(CommandGroup):

    def __init__(self, pipeline=1):
        super().__init__('Go To Tape')

        print("Has Hatch: "+str(robot.hatch.hasHatchPanel))

        @fc.IF(lambda: robot.hatch.hasHatchPanel())
        def placeHatch(self):
            print("Has hatch")
            self.addSequential(GoToTapeCommand(), 3)
            self.addSequential(HatchEjectCommand(), 0.3)
            self.addSequential(MoveCommand(-12))
            #self.addSequential(TimedMoveCommand(1, -0.3))
            #self.addSequential(SeizureLightsCommand(), 1.5)

        @fc.ELIF(lambda: not robot.hatch.hasHatchPanel())
        def grabHatch(self):
            print("No hatch")
            self.addParallel(HatchIntakeCommand(),3)
            self.addSequential(GoToTapeCommand())
            self.addSequential(MoveCommand(-12))
            #self.addSequential(TimedMoveCommand(1.5, 0.2))
            #self.addSequential(TimedMoveCommand(1, -0.3))
            #self.addSequential(SeizureLightsCommand(), 1.5)
