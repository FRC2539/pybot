from wpilib.command.timedcommand import TimedCommand

import subsystems

class IndexCommand(TimedCommand):

    def __init__(self):
        super().__init__('Outtake', 1)

        self.requires(subsystems.index)


    def initialize(self):
        subsystems.index.shoot()


    def end(self):
        subsystems.index.stop()
