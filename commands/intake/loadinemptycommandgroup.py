import commandbased.flowcontrol as fc

from commands.intake.intakecommand import IntakeCommand
from commands.revolver.ensureemptinesscommand import EnsureEmptinessCommand

class LoadInEmptyCommandGroup(fc.CommandFlow):

    def __init__(self):
        super().__init__('Load In Empty')

        #self.addParallel(IntakeCommand())
        self.addParallel(EnsureEmptinessCommand())
