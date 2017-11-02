from wpilib.command.commandgroup import CommandGroup
from .turnandgocommand import TurnAndGoCommand

class FaceLiftCommand(CommandGroup):
    '''
    Calculates the needed turn based on the vision target offset, then performs
    a single turn to make the needed correction.
    '''

    def __init__(self):
        super().__init__('Face Lift')

        readCamera = TurnAndGoCommand()
        self.addSequential(readCamera)
        self.addSequential(readCamera.turn())
