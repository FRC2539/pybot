from wpilib.command.instantcommand import InstantCommand

import robot

class ResetElevatorCommand(InstantCommand):

    def __init__(self):
        super().__init__('Reset Elevator')

        self.requires(robot.elevator)
        self.setRunWhenDisabled(True)


    def initialize(self):
        robot.elevator.reset()
