from wpilib.command.command import Command

import robot

class ForceLowerCommand(Command):

    def __init__(self):
        super().__init__('Force Lower')

        self.requires(robot.elevator)


    def initialize(self):
        robot.elevator.forceDown()


    def end(self):
        robot.elevator.stop()
