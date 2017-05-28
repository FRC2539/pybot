from wpilib.command.commandgroup import CommandGroup

from ..alertcommand import AlertCommand
from ..drive.setspeedcommand import SetSpeedCommand
from ..drive.runintowallcommand import RunIntoWallCommand
from wpilib.command.waitcommand import WaitCommand

class BlindHangCommandGroup(CommandGroup):
    '''
    Runs if the autonomous program can't see a gear. Drives forward until it
    hits something.
    '''

    def __init__(self):
        super().__init__('Blind Gear Hang')

        self.addSequential(AlertCommand('Attempting Blind Hang'))
        self.addSequential(SetSpeedCommand(300))
        self.addSequential(RunIntoWallCommand(35, 7))
        self.addSequential(AlertCommand('Finished Blind Hang'))
