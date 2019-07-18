from wpilib.command.command import Command

import robot

class DropCommand(Command):

    def __init__(self):
        super().__init__('Drop')

        self.requires(robot.dropper)


    def initialize(self):
        pass


    def execute(self):
        pass


    def end(self):
        pass
