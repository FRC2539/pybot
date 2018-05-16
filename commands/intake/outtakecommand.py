from wpilib.command.timedcommand import TimedCommand

import subsystems

class OuttakeCommand(TimedCommand):

    def __init__(self):
        super().__init__('Outtake', 2)

        self.requires(subsystems.intake)


    def initialize(self):
        subsystems.intake.outtake()


    def end(self):
        subsystems.intake.stop()
