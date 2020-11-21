from wpilib.command import InstantCommand

import robot

class DisableAutoCheckCommand(InstantCommand):

    def __init__(self):
        super().__init__('Disable Auto Check')

        self.requires(robot.revolver)

    def initialize(self):
        robot.revolver.disableDefaultChecking()


