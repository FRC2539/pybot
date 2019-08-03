from wpilib.command.commandgroup import CommandGroup
import commandbased.flowcontrol as fc

import robot

from commands.lights.seizurelightscommand import SeizureLightsCommand

from commands.drivetrain.gototapecommand import GoToTapeCommand
from commands.drivetrain.gopasttapecommand import GoPastTapeCommand
from commands.drivetrain.transitionmovecommand import TransitionMoveCommand
from commands.drivetrain.movecommand import MoveCommand

from commands.resetcommand import ResetCommand


class GoToTapeCommandGroup(CommandGroup):

    def __init__(self, pipeline=1):
        super().__init__('Go To Tape')

        self.addSequential(GoToTapeCommand())

        '''

        Rewrite for cargo!

        # Add commands here with self.addSequential() and self.addParallel()
        @fc.IF(lambda: not robot.hatch.hasHatchPanel())
        def grabHatch(self):
            self.addParallel(HatchIntakeCommand())
            self.addSequential(GoToTapeCommand(pipeline))
            self.addParallel(HatchIntakeCommand(True), 2)
            self.addSequential(GoPastTapeCommand(), 0.25)
            self.addParallel(SeizureLightsCommand(), 3)
            self.addSequential(TransitionMoveCommand(-100,-100,-12,-12,0,0))
            self.addSequential(ResetCommand())

        @fc.ELIF(lambda: robot.hatch.hasHatchPanel())
        def placeHatch(self):
            self.addSequential(GoToTapeCommand(pipeline))
            self.addSequential(GoPastTapeCommand(), 0.25)
            self.addParallel(HatchEjectCommand())
            self.addParallel(SeizureLightsCommand(), 3)
            self.addSequential(TransitionMoveCommand(-100,-100,-12,-12,0,0))
            self.addSequential(ResetCommand())

        '''
