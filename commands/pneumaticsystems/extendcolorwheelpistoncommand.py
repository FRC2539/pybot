from wpilib.command import Command

import robot

class ExtendColorWheelPistonCommand(Command):

    def __init__(self):
        super().__init__('Extend Color Wheel Piston')

        self.requires(robot.pneumaticsystems)


    def initialize(self):
        pass


    def execute(self):
        pass


    def end(self):
        pass
