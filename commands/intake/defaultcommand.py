from wpilib.command.command import Command

import robot

class DefaultCommand(Command):

    def __init__(self):
        super().__init__('Default for Intake')

        self.requires(robot.intake)


    def initialize(self):
        robot.intake.stopTake()
