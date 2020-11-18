from wpilib.command import InstantCommand

import robot

class EnableAutoCheckCommand(InstantCommand):

    def __init__(self):
        super().__init__('Enable Auto Check')

        self.requires(robot.revolver)

    def initialize(self):
        robot.revolver.enableDefaultChecking()
