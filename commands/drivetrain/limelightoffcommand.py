from wpilib.command.command import Command

import robot

class limeLightOffCommand(Command):

    def __init__(self):
        super().__init__('lime Light Off')

        self.requires(robot.hatch)


    def initialize(self):
        robot.hatch.limeLightOff()


    def execute(self):
        pass


    def end(self):
        pass
