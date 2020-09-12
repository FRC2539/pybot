from wpilib.command import InstantCommand

import robot


class DecreaseHoodAdjustmentCommand(InstantCommand):

    def __init__(self):
        super().__init__('Decrease Hood Adjustment')

        self.requires(robot.hood)


    def initialize(self):
        robot.hood.decreaseAdjustment(1)


