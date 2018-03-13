from wpilib.command.timedcommand import TimedCommand

import subsystems

class SlowOuttakeCommand(TimedCommand):

    def __init__(self):
        super().__init__('Slow Outtake', 1)

        self.requires(subsystems.intake)


    def initialize(self):
        subsystems.intake.slowOut()


    def end(self):
        subsystems.intake.stopTake()
