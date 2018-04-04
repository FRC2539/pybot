from wpilib.command.command import Command
from wpilib.timer import Timer

import subsystems

class IntakeCommand(Command):

    def __init__(self):
        super().__init__('Intake')

        self.requires(subsystems.intake)


    def initialize(self):
        subsystems.intake.intake()
        self.endTime = None


    def isFinished(self):
        if self.endTime:
            return self.endTime < Timer.getFPGATimestamp()
        else:
            if subsystems.intake.isCubeInIntake():
                # Wait 1 second after cube detected
                self.endTime = Timer.getFPGATimestamp() + 1

        return False


    def end(self):
        subsystems.intake.stopTake()
