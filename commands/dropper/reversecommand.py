from wpilib.command.command import Command

import robot

class ReverseCommand(Command):

    def __init__(self):
        super().__init__('Reverse')

        self.requires(robot.dropper)


    def initialize(self):
        robot.dropper.returnObject()


    def end(self):
        robot.dropper.stop()
