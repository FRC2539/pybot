from wpilib.command import Command

import robot

class TurretFieldOrientedCommand(Command):

    def __init__(self):
        super().__init__('Turret Field Oriented')

        self.requires(robot.turret)

    def initialize(self):
        robot.turret.captureOrientation()
        robot.turret.turretFieldOriented()

    def execute(self):
        robot.turret.turretFieldOriented()

    def end(self):
        robot.turret.stop()
