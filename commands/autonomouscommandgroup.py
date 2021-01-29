import commandbased.flowcontrol as fc

from commands.drivetrain.turncommand import TurnCommand

class AutonomousCommandGroup(fc.CommandFlow):
    def __init__(self):
        super().__init__("Autonomous")

        self.addSequential(TurnCommand(90))
