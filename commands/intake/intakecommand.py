from wpilib.command.command import Command
from wpilib.timer import Timer

import subsystems

class IntakeCommand(Command):

    def __init__(self):
        super().__init__('Intake')

        self.requires(subsystems.intake)


    def initialize(self):
        subsystems.intake.intake()
        subsystems.index.intake()


    def end(self):
        subsystems.intake.stop()
        subsystems.index.stop()
