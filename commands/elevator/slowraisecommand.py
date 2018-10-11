from wpilib.command.command import Command

import robot

class SlowRaiseCommand(Command):

    def __init__(self):
        super().__init__('Slow Raise')

        self.requires(robot.elevator)


    def initialize(self):
        robot.elevator.slowElevate()


    def end(self):
        robot.elevator.stop()
