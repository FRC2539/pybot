from wpilib.command import InstantCommand

import robot

class DisableCompessorCommand(InstantCommand):

    def __init__(self):
        super().__init__('Disable Compessor')

    def initialize(self):
        robot.pneumatics.disableCLC()
        robot.pneumatics.stopCompressor()
