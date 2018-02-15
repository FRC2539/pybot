from wpilib.command.instantcommand import InstantCommand

import subsystems

class ChangeLevelCommand(InstantCommand):

    def __init__(self, step=1):
        super().__init__('Change Level by %d' % step)

        self.requires(subsystems.elevator)
        self.step = step


    def initialize(self):
        subsystems.elevator.changeLevel(self.step)
