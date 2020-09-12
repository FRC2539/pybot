from wpilib.command import InstantCommand

import robot


class DecreaseTurretAdjustmentCommand(InstantCommand):

    def __init__(self):
        super().__init__('Decrease Turret Adjustment')

        self.requires(robot.turret)


    def initialize(self):
        robot.turret.decreaseAdjustment(1)


