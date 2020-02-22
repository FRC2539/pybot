from wpilib.command import Command

import robot


class SetTurretCommand(Command):

    def __init__(self, val):
        super().__init__('Set Turret')

        self.requires(robot.turret)
        self.target = val


    def initialize(self):
        pass

    def execute(self):
        robot.turret.setPosition(self.target)


    def end(self):
        robot.turret.stop()
