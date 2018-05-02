from wpilib.command.instantcommand import InstantCommand

import robot

class ChangeLevelCommand(InstantCommand):

    def __init__(self, step=1):
        super().__init__('Change Level by %d' % step)

        self.requires(robot.elevator)
        self.step = step


    def initialize(self):
        robot.elevator.changeLevel(self.step)
