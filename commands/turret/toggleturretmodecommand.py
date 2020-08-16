from wpilib.command import InstantCommand

import robot

class ToggleTurretModeCommand(InstantCommand):

    def __init__(self):
        super().__init__('Toggle Turret Mode')

    def initialize(self):
        robot.turret.turretActiveMode = not robot.turret.turretActiveMode
