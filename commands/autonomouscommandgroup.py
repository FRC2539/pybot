import commandbased.flowcontrol as fc

from crapthatwillneverwork.trajectorycommand import TrajectoryCommand

trajCommand = TrajectoryCommand(0)

class AutonomousCommandGroup(fc.CommandFlow):

    def __init__(self):
        super().__init__('Autonomous')

        self.addSequential(trajCommand())

        # Add commands here with self.addSequential() and self.addParallel()
