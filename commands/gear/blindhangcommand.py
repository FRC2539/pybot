from wpilib.command.commandgroup import CommandGroup
from commandbased.stopcommand import StopCommand

from ..alertcommand import AlertCommand
from ..pickup.pickupcommand import PickupCommand
from ..drive.runintowallcommand import RunIntoWallCommand

class BlindHangCommand(CommandGroup):
    '''
    Runs if the autonomous program can't see a gear. Turns on pickup and drives
    forward until it hits something.
    '''

    def __init__(self):
        super().__init__('Blind Gear Hang')

        pickup = PickupCommand()
        self.addParallel(pickup)
        self.addSequential(AlertCommand('Attempting Blind Hang'))
        self.addSequential(RunIntoWallCommand(300))
        self.addSequential(StopCommand(pickup))
