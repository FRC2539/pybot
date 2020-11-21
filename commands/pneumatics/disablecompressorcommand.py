from wpilib.command import InstantCommand

import robot

class DisableCompressorCommand(InstantCommand):

    def __init__(self):
        super().__init__('Disable Compressor')

    def initialize(self):
        robot.pneumatics.override = True
        robot.pneumatics.disableCLC()
        robot.pneumatics.stopCompressor()
