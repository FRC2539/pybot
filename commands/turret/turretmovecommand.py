from wpilib.command import Command

import robot

from controller import logicalaxes

logicalaxes.registerAxis('turretX')

class TurretMoveCommand(Command):

    def __init__(self):
        super().__init__('turret Move')

        self.requires(robot.turret)

    def execute(self):
        direction = logicalaxes.turretX.get() * -0.75
        if (not robot.turret.isZeroed() and not robot.turret.isMax()) or \
            (robot.turret.isZeroed() and direction >= 0) or \
            (robot.turret.isMax() and direction <= 0):

            robot.turret.accelMove(direction)


    def end(self):
        robot.turret.stop()
