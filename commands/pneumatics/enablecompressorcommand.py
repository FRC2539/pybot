from wpilib.command import InstantCommand

import robot

class EnableCompessorCommand(InstantCommand):

    def __init__(self):
        super().__init__('Enable Compessor')

    def initialize(self):
        robot.pneumatics.enableCLC()
