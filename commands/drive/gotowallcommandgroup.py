from wpilib.command.commandgroup import CommandGroup

from .setspeedcommand import SetSpeedCommand
from .gotowallcommand import GoToWallCommand

class GoToWallCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Go To Wall')

        self.addSequential(SetSpeedCommand(300))
        self.addSequential(GoToWallCommand())
