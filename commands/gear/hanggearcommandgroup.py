from .turnandgocommand import TurnAndGoCommand
from .drivetoliftcommand import DriveToLiftCommand
from commands.drive.setspeedcommand import SetSpeedCommand
from .waitforliftcommand import WaitForLiftCommand
from wpilib.command.waitcommand import WaitCommand
from wpilib.command.commandgroup import CommandGroup

import subsystems
from custom.config import Config
import custom.flowcontrol as fc

class HangGearCommandGroup(CommandGroup):
    '''Hangs a gear on a peg in front of it.'''

    def __init__(self):
        super().__init__('Hang a gear')

        def outsideHandoffDistance():
            global subsystems

            distance = subsystems.gear.getLiftDistance()
            if distance is None:
                return False

            return distance > Config('Gear/HandOffDistance')

        @fc.IF(outsideHandoffDistance)
        def alignWithLift(self):
            readCamera = TurnAndGoCommand()
            self.addSequential(readCamera)
            self.addSequential(readCamera.turn())
            self.addSequential(readCamera.go())
            self.addSequential(WaitForLiftCommand())
            self.addSequential(WaitCommand(0.3))

        @fc.IF(subsystems.gear.isLiftVisible)
        def hangOnLift(self):
            readCamera = TurnAndGoCommand()
            self.addSequential(readCamera)
            self.addSequential(readCamera.turn())
            self.addSequential(SetSpeedCommand(600))
            self.addSequential(DriveToLiftCommand())
