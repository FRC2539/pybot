from wpilib.command.command import Command

import robot

class SlowLowerCommand(Command):

    def __init__(self):
        super().__init__('Slow Lower')

        self.requires(robot.elevator)


    def initialize(self):
        robot.elevator.slowLower()


    def end(self):
        robot.elevator.stop()
