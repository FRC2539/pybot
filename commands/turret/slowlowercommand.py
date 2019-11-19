from wpilib.command.command import Command

import robot

class SlowLowerCommand(Command):

    def __init__(self):
        super().__init__('Slow Lower')

        self.requires(robot.turret)


    def initialize(self):
        robot.turret.slowLower()

    def end(self):
        robot.turret.stop()
