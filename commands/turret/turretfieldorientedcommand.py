from wpilib.command import Command

import robot

class TurretFieldOrientedCommand(Command):

    def __init__(self):
        super().__init__('Turret Field Oriented')

        self.requires(robot.turret)
        self.requires(robot.ledsystem)

    def initialize(self):
        robot.ledsystem.setPurple()

    def execute(self):
        robot.turret.turretFieldOriented()

    def end(self):
        robot.turret.stop()
        robot.ledsystem.turnOff()
