import commandbased.flowcontrol as fc
from commands.drivetrain.curvecommand import CurveCommand
from commands.drivetrain.movecommand import MoveCommand
from commands.drivetrain.curveleftcommand import CurveLeftCommand


class PathTestCommandGroup(fc.CommandFlow):

    def __init__(self):
        super().__init__('Path Test')

        # Add commands here with self.addSequential() and self.addParallel()
        # self.addSequential(CurveCommand(Degrees, Radius, Right(true) or left(false)))
        self.addSequential(CurveCommand(250, 30, True))
        self.addSequential(CurveCommand(250, 30, False))

