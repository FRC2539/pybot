from wpilib.command import Command

import robot

from controller import logicalaxes

logicalaxes.registerAxis('turretX')

class TurretMoveCommand(Command):

    def __init__(self):
        super().__init__('turret Move')

        self.requires(robot.turret)

    def execute(self):
        direction = logicalaxes.turretX.get() * -0.85 # This is actually 75%; the deadband calculator in accelMove drops it by the deadband (0.1)
        if (not robot.turret.isLimitSwitch() and not robot.turret.isMin()) or \
            (robot.turret.isLimitSwitch() and direction >= 0) or \
            (robot.turret.isMin() and direction <= 0):

            robot.turret.accelMove(direction)

    def end(self):
        robot.turret.stop()
