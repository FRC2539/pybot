from wpilib.command.command import Command

import robot

class DownCommand(Command):

    def __init__(self):
        super().__init__('Down')

        self.requires(robot.arm)
        self.requires(robot.elevator)


    def initialize(self):
        self.elevatorDone = robot.elevator.down()
        self.armDone = robot.arm.down()


    def execute(self):
        if not self.elevatorDone:
            self.elevatorDone = robot.elevator.down()

        if not self.armDone:
            self.armDone = robot.arm.down()


    def end(self):
        robot.arm.stop()
        robot.elevator.stop()
