from wpilib.command import CommandGroup
from wpilib.command.waitcommand import WaitCommand
from commands.intake.outtakecommand import OuttakeCommand
from commands.index.indexcommand import IndexCommand

import subsystems

class ShootCommandGroup(CommandGroup):

    def __init__(self):
        super().__init__('Shoot')

        self.addParallel(OuttakeCommand())
        self.addSequential(WaitCommand(1))
        self.addSequential(IndexCommand())
