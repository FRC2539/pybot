from wpilib.command.command import Command

import robot

class LaunchCommand(Command):

    def __init__(self):
        super().__init__('Launch')

        self.requires(robot.dropper)


    def initialize(self):
        robot.dropper.shoot()


    def end(self):
        robot.dropper.stop()
