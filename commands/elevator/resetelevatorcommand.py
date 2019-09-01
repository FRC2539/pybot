from wpilib.command.command import Command

import robot

class ResetElevatorCommand(Command):

    def __init__(self):
        super().__init__('Reset Elevator')

        self.requires(robot.elevator)


    def initialize(self):
        robot.elevator.zeroEncoder()
