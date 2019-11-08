from wpilib.command.commandgroup import CommandGroup
import commandbased.flowcontrol as fc

import robot

from commands.hatch.hatchintakecommand import HatchIntakeCommand
from commands.hatch.hatchejectcommand import HatchEjectCommand
from commands.hatch.defaultcommand import DefaultCommand

from commands.lights.seizurelightscommand import SeizureLightsCommand
#from commands.lights.solidredcommand import SolidRedCommand

from commands.drivetrain.gototapecommand import GoToTapeCommand
from commands.drivetrain.tapepidcommand import TapePIDCommand
from commands.drivetrain.tapepidhighcommand import tapePIDHighCommand
from commands.drivetrain.tapepidlowcommand import TapePIDLowCommand
from commands.drivetrain.gopasttapecommand import GoPastTapeCommand
from commands.drivetrain.transitionmovecommand import TransitionMoveCommand
#from commands.drivetrain.limelightoffcommand import limeLightOffCommand
from commands.resetcommand import ResetCommand


class TapePIDCommandGroup(CommandGroup):

    def __init__(self, pipeline=1):
        super().__init__('Tape P I D')

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

        @fc.ELIF(lambda: robot.hatch.hasHatchPanel() and robot.elevator.isLow())
        def firstLevel(self):
            self.addSequential(TapePIDLowCommand())
            self.addSequential(GoPastTapeCommand(), 0.25)
            self.addParallel(HatchEjectCommand())
            self.addParallel(SeizureLightsCommand(), 3)
            self.addSequential(TransitionMoveCommand(-100,-100,-12,-12,0,0))
            self.addSequential(ResetCommand())
        @fc.ELIF(lambda: robot.hatch.hasHatchPanel() and robot.elevator.isMid())
        def secondLevel(self):
            self.addSequential(TapePIDCommand())
            self.addSequential(GoPastTapeCommand(), 0.25)
            self.addParallel(HatchEjectCommand())
            self.addParallel(SeizureLightsCommand(), 3)
            self.addSequential(TransitionMoveCommand(-100,-100,-12,-12,0,0))
            self.addSequential(ResetCommand())
        @fc.ELIF(lambda: robot.hatch.hasHatchPanel() and robot.elevator.isHigh())
        def thridLevel(self):
            self.addSequential(tapePIDHighCommand())
            self.addSequential(GoPastTapeCommand(), 0.25)
            self.addParallel(HatchEjectCommand())
            self.addParallel(SeizureLightsCommand(), 3)
            self.addSequential(TransitionMoveCommand(-100,-100,-12,-12,0,0))
            self.addSequential(ResetCommand())
