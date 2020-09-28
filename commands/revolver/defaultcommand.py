from wpilib.command import Command

import robot


class DefaultCommand(Command):

    def __init__(self):
        super().__init__('Default for revolver')

        self.requires(robot.revolver)


    def initialize(self):
        pass


    def execute(self):
        pass


    def end(self):
        pass
