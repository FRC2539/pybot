from wpilib.command.command import Command

import robot

class DefaultCommand(Command):

    def __init__(self):
        super().__init__('Default for elevator')

        self.requires(robot.elevator)


    def initialize(self):
        self.position = robot.elevator.getPosition()


    def execute(self):
        robot.elevator.setPosition(self.position)


    def end(self):
        pass
