from wpilib.command import InstantCommand

import robot


class IncreaseHoodAdjustmentCommand(InstantCommand):

    def __init__(self):
        super().__init__('Increase Hood Adjustment')

        self.requires(robot.hood)


    def execute(self):
        robot.hood.increaseAdjustment(.1)
        robot.hood.updateNetworkTables()


