from wpilib.command import Command

import robot


class FieldOrientationTurretCommand(Command):

    def __init__(self):
        super().__init__('Field Orientation Turret')

        self.requires(robot.turret)


    def initialize(self):
        pass


    def execute(self):
        pass


    def end(self):
        pass
