from wpilib.command import Command

import robot

class DefaultCommand(Command):

    def __init__(self):
        super().__init__('Default for hood')

        self.requires(robot.hood)


    def execute(self):
        robot.hood.getEnc()

