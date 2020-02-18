from wpilib.command.command import Command

import robot

class ZeroTurretCommand(Command):

    def __init__(self):
        super().__init__('Zero Turret')

        self.requires(robot.turret)

    def initialize(self):
        pass


    def execute(self):
        if (robot.turret.getPosition!=0):
            robot.turret.move(.1)
        else:
            robot.turret.stop()


    def end(self):
        robot.turret.stop()
