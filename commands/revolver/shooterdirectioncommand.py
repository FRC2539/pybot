from wpilib.command import Command

import robot

class ShooterDirectionCommand(Command):

    def __init__(self):
        super().__init__('Set Speed')

        self.requires(robot.revolver)

    def initialize(self):
        robot.revolver.setStaticSpeed()

    def end(self):
        robot.revolver.stopRevolver()
