import commandbased.flowcontrol as fc

from commands.ballsystem.runallcommand import RunAllCommand
from commands.ballsystem.runallslowcommand import RunAllSlowCommand

from commands.intake.intakecommand import IntakeCommand

from commands.hood.activesethoodcommand import ActiveSetHoodCommand
from commands.shooter.shootcommand import ShootCommand

class SlowRunBallFlowCommandGroup(fc.CommandFlow):

    def __init__(self):
        super().__init__('Slow Run Ball Flow')

        self.addParallel(RunAllCommand())
        self.addParallel(IntakeCommand(0.15))
        self.addParallel(ShootCommand(500))
        # Add commands here with self.addSequential() and self.addParallel()
