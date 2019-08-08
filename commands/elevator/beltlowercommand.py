from wpilib.command.command import Command

import robot

class BeltLowerCommand(Command):

    def __init__(self):
        super().__init__('Belt Lower')

        self.requires(robot.elevator)


    def initialize(self):
        robot.elevator.singleLower()


    def end(self):
        robot.elevator.stop()
