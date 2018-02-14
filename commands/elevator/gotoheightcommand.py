from wpilib.command import Command

import subsystems

class GoToHeightCommand(Command):

    def __init__(self, level):
        super().__init__('GoToHeightCommand')
        self.level=level

        self.requires(subsystems.elevator)


    def initialize(self):
        subsystems.elevator.setLevel(self.level)
