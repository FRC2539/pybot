import commandbased.flowcontrol as fc

from commands.drivetrain.movecommand import MoveCommand

class AutonomousCommandGroup(fc.CommandFlow):
    def __init__(self):
        super().__init__("Autonomous")

        self.addSequential(MoveCommand(120))

        # Add commands here with self.addSequential() and self.addParallel()
