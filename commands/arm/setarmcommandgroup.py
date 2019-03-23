from wpilib.command.commandgroup import CommandGroup
import commandbased.flowcontrol as fc

from wpilib.command.waitcommand import WaitCommand

from commands.elevator.deelevatecommand import DeelevateCommand
from commands.elevator.bumpupcommand import BumpUpCommand

from commands.arm.lowercommand import LowerCommand
from commands.arm.downstagecommand import DownStageCommand
from commands.arm.upstagecommand import UpStageCommand

import robot

class SetArmCommandGroup(CommandGroup):

    def __init__(self, armTarget, eleTarget=0.0):
        super().__init__('Set Arm')

        # Add commands here with self.addSequential() and self.addParallel()

        #Make sure elevator is at end of travel.
        self.addSequential(DeelevateCommand())

        #Lower arm to end of travel.
        self.addSequential(LowerCommand())

        #Wait for ramp rate to finish up.
        self.addSequential(WaitCommand(.5))

        #Spam zero to make sure it actually works.
        self.addSequential(LowerCommand())
        self.addSequential(LowerCommand())
        self.addSequential(LowerCommand())
        self.addSequential(LowerCommand())
        self.addSequential(LowerCommand())

        #Remove any slack from the chain.
        self.addSequential(DownStageCommand())

        #Move elevator and arm to desired positions.
        @fc.IF(lambda: not eleTarget == 0.0)
        def eleMove(self):
            self.addParallel(BumpUpCommand(float(eleTarget)))
            self.addSequential(UpStageCommand(float(armTarget)))

        #Move arm to desired position.
        @fc.ELSE
        def noEleMove(self):
            self.addSequential(UpStageCommand(float(armTarget)))
