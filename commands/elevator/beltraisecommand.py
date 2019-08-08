from wpilib.command.command import Command

import robot

class BeltRaiseCommand(Command):

    def __init__(self):
        super().__init__('Belt Raise')

        self.requires(robot.elevator)


    def initialize(self):
        robot.elevator.singleRaise()


    def end(self):
        robot.elevator.stop()
