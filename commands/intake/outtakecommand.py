from wpilib.command import TimedCommand

import robot

class OutakeCommand(TimedCommand):
    def __init__(self):
        super().__init__('Outake', 2)

        self.requires(robot.intake)

    def initialize(self):
        robot.intake.outake()

    def end(self):
        robot.intake.stop()
