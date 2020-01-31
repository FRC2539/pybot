from wpilib.command import Command

import robot

class OutakeCommand(Command):
    def __init__(self):
        super().__init__('Outake', 1.5)

        self.requires(robot.intake)

    def initialize(self):
        robot.intake.outake()

    def end(self):
        robot.intake.stop() # Or maybe just stop it...