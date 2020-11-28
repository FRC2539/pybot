from wpilib.command import Command

import robot


class SpinUpRevolverCommand(Command):

    def __init__(self):
        super().__init__('Spin Up Revolver')

        self.requires(robot.revolver)
        
    def initialize(self):
        robot.revolver.setStaticSpeed()
