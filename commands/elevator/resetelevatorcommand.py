from wpilib.command import Command

import subsystems

class ResetElevatorCommand(Command):

    def __init__(self):
        super().__init__('Reset Elevator')

        self.requires(subsystems.elevator)
        self.setRunWhenDisabled(True)


    def initialize(self):
        subsystems.elevator.reset()
