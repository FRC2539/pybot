from wpilib.command.command import Command

import robot

class UpCommand(Command):

    def __init__(self):
        super().__init__('Up')

        self.requires(robot.arm)
        self.requires(robot.elevator)


    def initialize(self):
        self.elevatorDone = robot.elevator.up()
        self.armDone = robot.arm.up()


    def execute(self):
        if not self.elevatorDone:
            self.elevatorDone = robot.elevator.up()

        if not self.armDone:
            self.armDone = robot.arm.up()


    def end(self):
        robot.arm.stop()
        robot.elevator.stop()
