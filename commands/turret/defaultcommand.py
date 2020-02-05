from wpilib.command import Command

import robot

class DefaultCommand(Command):

    def __init__(self):
        super().__init__('Turret')

        self.requires(robot.turret)

    def execute(self):
        #robot.turret.pencoder()
        pass
