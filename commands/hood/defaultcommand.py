from wpilib.command import Command

import robot

class DefaultCommand(Command):

    def __init__(self):
        super().__init__('Default for hood')

        self.requires(robot.hood)


    def initialize(self):
        pass#print('pos  ' + str(robot.hood.getPosition()))

    def execute(self):
        pass#print('pos  ' + str(robot.hood.getPosition()))

    def end(self):
        pass
