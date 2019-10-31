from wpilib.command.commandgroup import CommandGroup
import commandbased.flowcontrol as fc

import robot

from commands.hatch.hatchintakecommand import HatchIntakeCommand
from commands.hatch.hatchejectcommand import HatchEjectCommand
from commands.hatch.defaultcommand import DefaultCommand

from commands.lights.seizurelightscommand import SeizureLightsCommand
#from commands.lights.solidredcommand import SolidRedCommand

from commands.drivetrain.testgototapecommand import TestGoToTapeCommand
from commands.drivetrain.gopasttapecommand import GoPastTapeCommand
from commands.drivetrain.transitionmovecommand import TransitionMoveCommand
#from commands.drivetrain.limelightoffcommand import limeLightOffCommand
from commands.resetcommand import ResetCommand


class TestGoToTapeCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Go To Tape')

        # Add commands here with self.addSequential() and self.addParallel()
        #@fc.IF(lambda: not robot.hatch.getTapeValue())
        #def checkHatch(self):
            ##self.addSequential(SolidRedCommand())
           ##self.addSequential(limeLightOffCommand())
           #pass
        @fc.IF(lambda: not robot.hatch.hasHatchPanel())
        def grabHatch(self):
            self.addParallel(HatchIntakeCommand())
            self.addSequential(TestGoToTapeCommand())
            self.addParallel(HatchIntakeCommand(True), 2)
            self.addSequential(GoPastTapeCommand(), 0.25)
            self.addParallel(SeizureLightsCommand(), 3)
            self.addSequential(TransitionMoveCommand(-100,-100,-12,-12,0,0))
            self.addSequential(ResetCommand())

        @fc.ELIF(lambda: robot.hatch.hasHatchPanel())
        def placeHatch(self):
            self.addSequential(TestGoToTapeCommand())
            self.addSequential(GoPastTapeCommand(), 0.25)
            self.addParallel(HatchEjectCommand())
            self.addParallel(SeizureLightsCommand(), 3)
            self.addSequential(TransitionMoveCommand(-100,-100,-12,-12,0,0))
            self.addSequential(ResetCommand())
