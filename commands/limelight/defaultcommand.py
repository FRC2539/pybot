from wpilib.command import Command

import robot

class DefaultCommand(Command):

    def __init__(self):
        super().__init__('Default for limelight')

        self.requires(robot.limelight)


    def initialize(self):
        robot.limelight.setPipeline(2)


    def execute(self):
        robot.limelight.updateNetworkTables()


    def end(self):
        pass
