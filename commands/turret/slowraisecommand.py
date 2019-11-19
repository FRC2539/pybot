from wpilib.command.command import Command

import robot

class SlowRaiseCommand(Command):

    def __init__(self):
        super().__init__('Slow Raise')

        self.requires(robot.turret)


    def initialize(self):
        robot.turret.slowRaise()

    def end(self):
        robot.turret.stop()
