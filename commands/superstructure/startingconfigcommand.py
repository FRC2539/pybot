from wpilib.command.command import Command

import robot

class StartingConfigCommand(Command):

    def __init__(self):
        super().__init__('Starting Config')

        self.requires(robot.arm)
        self.requires(robot.elevator)

    def initialize(self):
        robot.arm.goToStartingPosition()
        robot.elevator.goToFloor()


    def execute(self):
        pass


    def end(self):
        pass
