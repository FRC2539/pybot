from wpilib.command.command import Command

import robot


class SuperPidCommand(Command):

    def __init__(self, inches, degrees):
        super().__init__('Super Pid')

        self.requires(robot.elevator)
        self.requires(robot.arm)

        self.inches = inches
        self.degrees = degrees


    def initialize(self):
        if self.inches < 56.1 and self.inches > 0:
            robot.arm.positionPID(self.degrees)
            robot.elevator.setPosition(self.inches)
        elif self.inches ==0:
            robot.arm.positionPID(self.degrees)
        else:
            pass

    def execute(self):
        pass


    def end(self):
        pass
