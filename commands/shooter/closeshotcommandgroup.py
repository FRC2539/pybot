import commandbased.flowcontrol as fc

from commands.hood.activesethoodcommand import ActiveSetHoodCommand
from commands.shooter.shootcommand import ShootCommand


class CloseShotCommandGroup(fc.CommandFlow):

    def __init__(self):
        super().__init__('Close Shot')

        # Add commands here with self.addSequential() and self.addParallel()

        self.addParallel(ShootCommand(4200))
        self.addParallel(ActiveSetHoodCommand(155))
