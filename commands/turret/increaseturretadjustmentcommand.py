from wpilib.command import InstantCommand

import robot


class IncreaseTurretAdjustmentCommand(InstantCommand):

    def __init__(self):
        super().__init__('Increase Turret Adjustment')

        self.requires(robot.turret)


    def initialize(self):
        robot.turret.increaseAdjustment(1)


