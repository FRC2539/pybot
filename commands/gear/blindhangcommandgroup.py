from wpilib.command.commandgroup import CommandGroup
from commandbased.stopcommand import StopCommand

from ..alertcommand import AlertCommand
from ..pickup.pickupcommand import PickupCommand
from ..drive.setspeedcommand import SetSpeedCommand
from ..drive.runintowallcommand import RunIntoWallCommand
from wpilib.command.waitcommand import WaitCommand

class BlindHangCommandGroup(CommandGroup):
    '''
    Runs if the autonomous program can't see a gear. Turns on pickup and drives
    forward until it hits something.
    '''

    def __init__(self):
        super().__init__('Blind Gear Hang')

        #pickup = PickupCommand()
        #self.addParallel(pickup)
        self.addSequential(AlertCommand('Attempting Blind Hang'))
        self.addSequential(SetSpeedCommand(300))
        self.addSequential(RunIntoWallCommand(35, 7))
        self.addSequential(AlertCommand('Finished Blind Hang'))
        #self.addSequential(StopCommand(pickup))
