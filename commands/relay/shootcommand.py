from wpilib.command import Command

import robot

class ShootCommand(Command):

    def __init__(self):
        super().__init__('Shoot')

        self.requires(robot.relay)

    def initialize(self):
        robot.relay.setForward()

    def end(self):
        robot.relay.stop()
