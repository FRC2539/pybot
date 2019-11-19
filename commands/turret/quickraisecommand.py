from wpilib.command.command import Command

import robot

class QuickRaiseCommand(Command):

    def __init__(self):
        super().__init__('Quick Raise')

        self.requires(robot.turret)


    def initialize(self):
        robot.turret.raiseTurret()

    def end(self):
        robot.turret.stop()
