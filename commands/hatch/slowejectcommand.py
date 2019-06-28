from wpilib.command.command import Command

import robot

class SlowEjectCommand(Command):

    def __init__(self):
        super().__init__('Slow Eject')

        self.requires(robot.hatch)


    def initialize(self):
        robot.hatch.slowEject()


    def end(self):
        robot.hatch.hasHatch = False
        robot.hatch.stop()
