import commandbased.flowcontrol as fc

from commands.ballsystem.runallslowcommand import RunAllSlowCommand

from commands.intake.intakecommand import IntakeCommand

class SlowRunBallFlowCommandGroup(fc.CommandFlow):

    def __init__(self):
        super().__init__('Slow Run Ball Flow')

        self.addParallel(RunAllSlowCommand())
        self.addParallel(IntakeCommand(0.1))
        # Add commands here with self.addSequential() and self.addParallel()
