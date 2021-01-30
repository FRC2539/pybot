import commandbased.flowcontrol as fc

from commands.drivetrain.turncommand import TurnCommand
from commands.drivetrain.movecommand import MoveCommand


class AutonomousCommandGroup(fc.CommandFlow):
    def __init__(self):
        super().__init__("Autonomous")

        #self.addSequential(TurnCommand(90))
        self.addSequential(MoveCommand(100))
