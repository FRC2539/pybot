from wpilib.command import Command

import robot

class turretMoveCommand(Command):

    def __init__(self, speed):
        super().__init__('turret Move')

        self.requires(robot.turret)
        self.speed = speed

    def initialize(self):
        pass


    def execute(self):
        robot.turret.move(self.speed)


    def end(self):
        pass
