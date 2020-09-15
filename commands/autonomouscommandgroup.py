import commandbased.flowcontrol as fc

from crapthatwillneverwork.trajectorycommand import TrajectoryCommand
from crapthatwillneverwork.ramsetecommand import RamseteCommand

class AutonomousCommandGroup(fc.CommandFlow):
    
    def __init__(self):
        super().__init__('Autonomous')

        data = TrajectoryCommand(0).getCommand()

        self.addSequential(RamseteCommand(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]))

        # Add commands here with self.addSequential() and self.addParallel()
