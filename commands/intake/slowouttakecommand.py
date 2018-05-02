from wpilib.command.timedcommand import TimedCommand

import robot

class SlowOuttakeCommand(TimedCommand):

    def __init__(self):
        super().__init__('Slow Outtake', 1)

        self.requires(robot.intake)


    def initialize(self):
        robot.intake.slowOut()


    def end(self):
        robot.intake.stopTake()
