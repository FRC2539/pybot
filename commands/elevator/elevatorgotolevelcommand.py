from wpilib.command.command import Command

import robot

class ElevatorGoToLevelCommand(Command):

    def __init__(self, level):
        super().__init__('Elevator Go To Level')

        self.requires(robot.elevator)
        self.level = level


    def initialize(self):
        robot.elevator.goToLevel(self.level)
        print('went to level')

    def execute(self):
        pass


    def end(self):
        pass
