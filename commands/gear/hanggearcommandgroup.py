from wpilib.command import CommandGroup

from commands.gear.gotoliftcommand import GoToLiftCommand
from commands.gear.turntoliftcommand import TurnToLiftCommand

class HangGearCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('HangGearCommandGroup')

        self.addSequential(TurnToLiftCommand())
        self.addSequential(GoToLiftCommand())
