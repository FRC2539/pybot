from wpilib.command import Command

import robot

class RunCompressorCommand(Command):

    def __init__(self):
        super().__init__('PneumaticSystems')

        self.requires(robot.pneumaticsystems)

    def initialize(self):
        robot.pneumaticsystems.enableCompressor()

    def isFinished(self):
        print(robot.pneumaticsystems.isFull())
        return robot.pneumaticsystems.isFull()

    def end(self):
        robot.pneumaticsystems.disableCompressor()
