from wpilib.command.command import Command

import robot

class IndexForwardCommand(Command):

    def __init__(self):
        super().__init__('Index Forward')

        self.requires(robot.indexwheel)


    def initialize(self):
        robot.indexwheel.forward()

    def end(self):
        robot.indexwheel.stop()
