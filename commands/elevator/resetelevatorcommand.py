from wpilib.command import Command

import subsystems

class ResetElevatorCommand(Command):

    def __init__(self):
        super().__init__('Reset Elevator')

        self.requires(subsystems.elevator)


    def initialize(self):
        subsystems.elevator.reset()
