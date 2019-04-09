from wpilib.command.command import Command

import robot

class HatchEjectCommand(Command):

    def __init__(self):
        super().__init__('Hatch Eject')

        self.requires(robot.intake)


    def initialize(self):
        robot.intake.hatchEject()


    def end(self):
        robot.intake.stop()
