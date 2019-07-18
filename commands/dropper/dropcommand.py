from wpilib.command.command import Command

import robot

class DropCommand(Command):

    def __init__(self):
        super().__init__('Drop')

        self.requires(robot.dropper)


    def initialize(self):
        robot.dropper.slowDrop()


    def end(self):
        robot.dropper.stop()