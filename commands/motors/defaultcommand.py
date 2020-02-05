from wpilib.command.command import Command

import robot

class DefaultCommand(Command):

    def __init__(self):
        super().__init__('Default for motors')
        self.requires(robot.potentiometer)
        self.requires(robot.motors)

    def initialize(self):
        robot.motors.setMotors()

    def execute(self):
        robot.motors.setMotors()

