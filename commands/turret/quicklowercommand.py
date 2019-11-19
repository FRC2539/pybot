from wpilib.command.command import Command

import robot

class QuickLowerCommand(Command):

    def __init__(self):
        super().__init__('Quick Lower')

        self.requires(robot.turret)

    def initialize(self):
        robot.turret.lowerTurret()

    def end(self):
        robot.turret.stop()
