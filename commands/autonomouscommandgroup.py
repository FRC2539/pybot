from wpilib.command import CommandGroup
import commandbased.flowcontrol as fc
from custom.config import Config

from commands.drivetrain.holonomicmovecommand import HolonomicMoveCommand


class AutonomousCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Autonomous')

        #self.addSequential(HolonomicMoveCommand(70, 54, 45))
