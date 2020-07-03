import commandbased.flowcontrol as fc

from commands.ballsystem.detectandqueuecommand import DetectAndQueueCommand
from commands.intake.intakecommand import IntakeCommand

class IntakeAndQueueCommandGroup(fc.CommandFlow):

    def __init__(self):
        super().__init__('Intake And Queue')

        self.addParallel(IntakeCommand(0.45))
        self.addParallel(DetectAndQueueCommand())

        # Add commands here with self.addSequential() and self.addParallel()
