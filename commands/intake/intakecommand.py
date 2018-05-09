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


    def end(self):
        subsystems.intake.stopTake()
