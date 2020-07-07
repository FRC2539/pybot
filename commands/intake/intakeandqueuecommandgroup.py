import commandbased.flowcontrol as fc

from commands.ballsystem.detectandqueuecommand import DetectAndQueueCommand
from commands.intake.intakecommand import IntakeCommand
from commands.shooter.shootcommand import ShootCommand

class IntakeAndQueueCommandGroup(fc.CommandFlow):

    def __init__(self):
        super().__init__('Intake And Queue')

        self.addParallel(IntakeCommand(0.35))
        self.addParallel(DetectAndQueueCommand())

        # Add commands here with self.addSequential() and self.addParallel()
