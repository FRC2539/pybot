from wpilib.command.instantcommand import InstantCommand

import robot

class ElevatorResetCommand(InstantCommand):

    def __init__(self):
        super().__init__('Elevator Reset')

        self.requires(robot.elevator)


    def initialize(self):
        robot.elevator.reset()
