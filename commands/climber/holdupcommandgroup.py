from wpilib.command.commandgroup import CommandGroup
import commandbased.flowcontrol as fc

from commands.climber.doubleclimbcommand import DoubleClimbCommand
from commands.climber.maintainpositioncommand import MaintainPositionCommand

class HoldUpCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Hold Up')

        self.addSequential(DoubleClimbCommand())
        print('Done with one')

        self.addSequential(MaintainPositionCommand())

