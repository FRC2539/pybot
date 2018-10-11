from wpilib.command.command import Command

import robot

class IndexReverseCommand(Command):

    def __init__(self):
        super().__init__('Index Reverse')

        self.requires(robot.indexwheel)


    def initialize(self):
        robot.indexwheel.slowForward()

    def end(self):
        robot.indexwheel.stop()
