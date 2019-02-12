from wpilib.command.command import Command

import robot

class RaiseCommand(Command):

    def __init__(self):
        super().__init__('Raise')

        self.requires(robot.arm)


    def initialize(self):
        robot.arm.up()


    def execute(self):
        pass


    def end(self):
        robot.arm.stop()
