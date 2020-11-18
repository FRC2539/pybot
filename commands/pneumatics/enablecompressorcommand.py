from wpilib.command import InstantCommand

import robot

class EnableCompressorCommand(InstantCommand):

    def __init__(self):
        super().__init__('Enable Compressor')

    def initialize(self):
        robot.pneumatics.enableCLC()
