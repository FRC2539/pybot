from wpilib.command import Command

import robot

class DeelevateCommand(Command):

    def __init__(self):
        super().__init__('Deelevate')

        self.requires(robot.elevator)


    def initialize(self):
        robot.elevator.down()


    def end(self):
        robot.elevator.stop()
