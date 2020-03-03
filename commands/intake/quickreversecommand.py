from wpilib.command import TimedCommand

import robot

class QuickReverseCommand(TimedCommand):

    def __init__(self):
        super().__init__('Quick Reverse', 0.125)

        self.requires(robot.intake)

    def initialize(self):
        robot.intake.fumbleReverse()

    def end(self):
        robot.intake.stop()
