from wpilib.command.command import Command

import robot

class movehookCommand(Command):

    def __init__(self, speed):
        super().__init__('movehook')

        self.requires(robot.climbhook)
        self.speed = speed


    def initialize(self):
        robot.climbhook.moveHook(self.speed)


    def execute(self):
        pass


    def end(self):
        robot.climbhook.moveHook(0)
