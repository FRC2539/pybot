import commandbased.flowcontrol as fc
from commands.drivetrain.curvecommand import CurveCommand
from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.curveleftcommand import CurveLeftCommand


class PathTestCommandGroup(fc.CommandFlow):

    def __init__(self):
        super().__init__('Path Test')

        # Add commands here with self.addSequential() and self.addParallel()
        self.addSequential(CurveCommand(160, 40), 3)
        self.addSequential(CurveLeftCommand(160, 40), 3)
