from wpilib.command.command import Command

import robot

class RemoveCommand(Command):

    def __init__(self):
        super().__init__('Remove')

        self.requires(robot.intake)


    def initialize(self):
        robot.intake.reverse()


    def end(self):
        robot.intake.stop()
