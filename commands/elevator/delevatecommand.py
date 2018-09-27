from wpilib.command.command import Command

import robot

class DelevateCommand(Command):

    def __init__(self):
        super().__init__('Delevate')

        self.requires(robot.elevator)


    def initialize(self):
        robot.elevator.down()


    def end(self):
        robot.elevator.stop()
