from wpilib.command import InstantCommand

import robot


class IncreaseTurretAdjustmentCommand(InstantCommand):

    def __init__(self):
        super().__init__('Increase Turret Adjustment')

        self.requires(robot.turret)


    def execute(self):
        robot.turret.increaseAdjustment(.1)
        robot.turret.updateNetworkTables()

