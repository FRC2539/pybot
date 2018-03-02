from wpilib.command.timedcommand import TimedCommand

import subsystems

class TimedIntakeCommand(TimedCommand):

    def __init__(self):
        super().__init__('Timed Intake')

        self.requires(subsystems.intake)


    def initialize(self):
        subsystems.intake.intake()
