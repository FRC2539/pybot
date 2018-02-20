from wpilib.command.instantcommand import InstantCommand

import subsystems

class ResetElevatorCommand(InstantCommand):

    def __init__(self):
        super().__init__('Reset Elevator')

        self.requires(subsystems.elevator)
        self.setRunWhenDisabled(True)


    def initialize(self):
        subsystems.elevator.reset()
