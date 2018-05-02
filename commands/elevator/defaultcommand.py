from wpilib.command.command import Command

import robot

class DefaultCommand(Command):

    def __init__(self):
        super().__init__('Default for Elevator')

        self.requires(robot.elevator)
